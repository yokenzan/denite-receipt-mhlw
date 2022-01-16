from pynvim import Nvim

from denite.base.kind import Base
import denite.util
from denite.util import UserContext, Candidate


class Kind(Base):

    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)

        self.name = 'receipt-master'
        self.default_action = 'append'

    def action_append(self, context: UserContext) -> None:

    def action_yank(self, context: UserContext) -> None:
        self.action_yank_name(context)

    def action_yank_name(self, context: UserContext) -> None:
        _yank(self.vim, "\n".join([
            x['name'] for x in context['targets']
            ]))

    def action_yank_code(self, context: UserContext) -> None:
        _yank(self.vim, "\n".join([
            x['code'] for x in context['targets']
            ]))

    def action_yank_kana(self, context: UserContext) -> None:
        _yank(self.vim, "\n".join([
            x['kana'] for x in context['targets']
            ]))

    def action_yank_all(self, context: UserContext) -> None:
        _yank(self.vim, "\n".join([
            x['word'] for x in context['targets']
            ]))


def _yank(vim: Nvim, word: str) -> None:
    vim.call('setreg', '"', word, 'v')
    if vim.call('has', 'clipboard'):
        vim.call('setreg', vim.eval('v:register'), word, 'v')
