from display import DisplayBoard, welcome

from input import Interact, PlayGame

inter = Interact()
db = DisplayBoard()
welcome()
inter.player_count()
pg = PlayGame(inter)


while inter.playing:
    db.print_board(db.position)
    if inter.playing:
        inter.get_input()
    pg.game_over(inter)
    if not inter.playing:
        db.print_board(db.position)
        break
