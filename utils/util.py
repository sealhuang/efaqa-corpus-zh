# vi: set ft=python sts=4 ts=4 sw=4 et:

import os
import json
import gzip


def export_chats(raw_info, opt_file):
    """Export chats to `opt_file` from raw data."""
    with open(opt_file, 'w') as optf:
        for item in raw_info:
            optf.write('\ntitle: %s\n'%(item['title']))
            chat_list = item['chats']
            for line in chat_list:
                optf.write('%s：%s\n'%(line['sender'], line['value']))


if __name__ == '__main__':
    # load dataset
    root_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.path.pardir)
    )
    db_file = os.path.join(root_dir, 'data', 'efaqa-corpus-zh.utf8.gz')
    with gzip.open(db_file) as f:
        raw_data = f.readlines()
        raw_data = [json.loads(line) for line in raw_data]

    export_chats(raw_data, 'psychats.txt')

