from pynvim import Nvim
import os
import csv
import jaconv

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
            lambda si: self.generate_candidate(si),
            self.silist))

    def generate_candidate(self, si):
        kata   = jaconv.h2z(si['kana'])
        hira   = jaconv.kata2hira(kata)
        romaji = jaconv.kata2alphabet(kata).replace('ー', '-')
        return {
            'word':   " | ".join([si['code'], si['name'], romaji, hira]),
            'name':   si['name'],
            'code':   si['code'],
            'kana':   hira,
            'romaji': romaji,
        }
