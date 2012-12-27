import sys
import os

SYS_EXIT_CONF_CREATED = 10


class ConfFileManager:

    FNAME = "auto_versionning.conf"

    def __init__(self):
        if(os.path.exists(self.FNAME)):
            # then read
            pass
        else:
            # then create
            pass
            conf = {}
            conf["last_version"] = None
            conf["files"] = [{"path":"path/to/file", "format":"full"},
                            {"path":"path/to/file", "format":"full"}]

            with open(self.FNAME, 'w+') as f:
                f.write(json.dumps(conf))

