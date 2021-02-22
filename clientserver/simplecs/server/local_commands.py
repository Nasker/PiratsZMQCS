from simplecs.server.commands import Command, CommandSet


class LocalCommand(Command):
    # Just a base class that defines where the module is, so it does not have to be defined on every command
    # In this example does not make much sense because there is only one command

    @property
    def module(self):
        return self.app.server


class ListCommands(LocalCommand):
    ID = 0xFF01

    def execute(self):
        all_commands = {'local': list(LocalCommands.get_command_list())}
        return all_commands


class GetPubStats(LocalCommand):
    ID = 0xFF10

    def execute(self):
        stats = self.app.server.stats
        self.app.server.pub_async('pub_stats', stats)
        return stats


class LocalCommands(CommandSet):

    # When updating this list, simplecs.client.client should be updated
    _commands_available = {
        "get_pub_stats": GetPubStats,
        "list": ListCommands,
    }

    @classmethod
    def find_command_by_id(cls, command_id):
        find_command = [command for command_name, command in cls._commands_available.items() if
                        command.ID == command_id]
        if not len(find_command):
            raise Exception("Not found command: {}".format(hex(int(command_id))))
        return find_command[0]
