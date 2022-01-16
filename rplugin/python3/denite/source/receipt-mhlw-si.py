# ============================================================================
# FILE: source.py
# AUTHOR: Prabir Shrestha <mail at prabir.me>
# License: MIT license
# ============================================================================

from pynvim import Nvim
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
        with open('/home/yosuke/wk/repos/denite-receipt-master/csv/s.csv', 'r', encoding='shift_jis') as f:
            reader      = csv.reader(f)
            self.silist = list(map(
                lambda si: { 'code': si[2], 'name': si[4], 'kana': si[6] },
                    [row for row in reader]
                    ))

    def gather_candidates(self, context: UserContext) -> Candidates:
        return list(map(
            lambda si: {
                'word': " | ".join([si['code'], si['name'], si['kana'], ]),
                'name': si['name'],
                'code': si['code'],
                'kana': si['kana'],
                },
                self.silist))
