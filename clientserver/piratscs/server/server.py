from piratscs.logger import get_logger
from zmqcs.server import zmqServer
import traceback
from piratscs.server.local_commands import LocalCommands, Command

log = get_logger('server')


class Server(zmqServer):

    def __init__(self, app, cmd_port=None, async_port=None):
        self.app = app
        cmd_port = cmd_port or app.conf.server_ports.cmd_port
        async_port = async_port or app.conf.server_ports.async_port
        super().__init__(cmd_port=cmd_port, async_port=async_port)

    @staticmethod
    def _execute_local_command(command):
        assert isinstance(command, Command)
        result = command.execute()
        return result

    def execute_command(self, cmd_msg):
        """
        :param cmd_msg: is an instance of CommandMSG. It contains both the command name as well as the arguments
        :return: Must return a json serializable value. The output of the requested command or an exception
        """
        # This function is executed inside a try catch on the ZMQServer. If an exception is catched, the error
        # field of the answer will be filled

        if cmd_msg.command.startswith('local.'):
            cmd = cmd_msg.command[6:]
            command_class = LocalCommands.find_command_by_name(cmd)
            if command_class:
                try:
                    ret = self._execute_local_command(command_class(app=self.app, **cmd_msg.kwargs))
                except Exception:
                    log.exception(f"Exception while executing local command: {cmd_msg.command}")
                    self.pub_cmd_ret({'cmd': cmd_msg.command, 'error': traceback.format_exc()})
                    raise
                else:
                    self.pub_cmd_ret({'cmd': cmd_msg.command, 'ans': ret})
                    return ret
            else:
                raise Exception(f"Unknown local command {cmd}")
        else:
            return self.app.mod_handler.execute_command(cmd_msg)
        # else:
        #     raise Exception(f"Unknown command {cmd_msg.command}")

    def initialize(self):
        self.init_sockets()

    def pub_cmd_ret(self, cmdans):
        self.pub_async('app_cmd', cmdans)
