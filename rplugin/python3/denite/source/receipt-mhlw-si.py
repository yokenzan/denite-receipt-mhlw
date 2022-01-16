from pynvim import Nvim
import os
import csv

from denite.base.source import Base
from denite.util import UserContext, Candidates


class Source(Base):

    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)

        self.name   = 'receipt-mhlw-si'
        self.kind   = 'receipt-mhlw'
        self.silist = list()

    def on_init(self, context: UserContext) -> None:
        csvpath = os.path.relpath('/'.join([__file__] + ['..'] * 5 + ['csv/s.csv']))
        print(csvpath)
        with open(csvpath, 'r', encoding='shift_jis') as f:
            reader      = csv.reader(f)
            self.silist = list(map(
                lambda si: { 'code': si[2], 'name': si[4], 'kana': si[6] },
                    [row for row in reader]
                    ))

    def gather_candidates(self, context: UserContext) -> Candidates:
        return list(map(
            lambda si: {
                'word': " | ".join([si['code'], si['name'].ljust(64), si['kana'].ljust(20), ]),
                'name': si['name'],
                'code': si['code'],
                'kana': si['kana'],
                },
                self.silist))
