import ranger.api
import subprocess
from ranger.api.commands import *

HOOK_INIT_OLD = ranger.api.hook_init


def hook_init(fm):
    def update_autojump(signal):
        subprocess.Popen(["autojump", "--add", signal.new.path])

    fm.signal_bind("cd", update_autojump)
    HOOK_INIT_OLD(fm)

ranger.api.hook_init = hook_init


class j(Command):
    """:j [<text>]

    Uses autojump to set the current directory.

    It works in the same way as the `j` function provided by autojump. In
    addition, if fzf is present on the system, it is used to browse the
    completion proposals returned by autojump.
    """

    def execute(self):
        import os.path
        import re
        from ranger.ext.get_executables import get_executables

        if "autojump" not in get_executables():
            return self.fm.notify("Could not find autojump in the PATH.", bad=True)

        if "fzf" not in get_executables():
            directory = subprocess.check_output(["autojump", self.arg(1)])
            directory = directory.decode("utf-8", "ignore")
            directory = directory.rstrip("\n")
            self.fm.cd(directory)
        else:
            autojump = self.fm.execute_command(
                " ".join(["autojump --complete", self.arg(1)]),
                universal_newlines=True,
                stdout=subprocess.PIPE,
            )
            autojump_stdout, autojump_stderr = autojump.communicate()

            if autojump.returncode == 0:
                if autojump_stdout.rstrip("\n"):
                    fzf = self.fm.execute_command(
                        " ".join(
                            [
                                "autojump --complete",
                                self.arg(1),
                                "| fzf --no-multi --layout=reverse --ansi 2>/dev/tty",
                            ]
                        ),
                        universal_newlines=True,
                        stdout=subprocess.PIPE,
                    )
                    fzf_stdout, fzf_stderr = fzf.communicate()

                    if fzf.returncode == 0:
                        fzf_file = fzf_stdout.rstrip("\n")
                        fzf_file_path = re.sub(self.arg(1) + "__[1-9]__", "", fzf_file)
                        # print(fzf_file_path)
                        if os.path.isdir(fzf_file_path):
                            self.fm.cd(fzf_file_path)
                        else:
                            self.fm.select_file(fzf_file_path)
                else:  # sdtout is empty
                    return self.fm.notify(
                        "autojump: no match found for `%s`" % self.arg(1), bad=True
                    )

