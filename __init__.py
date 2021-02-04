# Michael's reset lapses add-on for anki 2.1.x
from anki.hooks import addHook
from aqt import *
from aqt.utils import tooltip

def onResetLapses(self):

    cids = self.selectedCards()
    if not cids:
        tooltip("No cards selected. :(")
        return

    for n in cids:
        card = self.mw.col.getCard(n)
        card.lapses = 0
        card.flush()

    tooltip("The lapses have been reset. :)")

def menuItem(self):
    menu = self.form.menu_Cards
    menu.addSeparator()

    a = menu.addAction('Reset Lapses')
    a.triggered.connect(lambda _, b=self: onResetLapses(b))

addHook("browser.setupMenus", menuItem)
