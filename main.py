import pygame
from partie import Partie

#initialisation des different pion

info_pion = {}
color = ["blanc", "noir"]
type_pion = ["soldat", "tour", "cavalier", "fou", "reine", "roi"]
nombre_pion = [8, 2, 2, 2, 1, 1]

for i in range(2):
    liste = []
    pion = {}
    for j, valeur in enumerate(type_pion):
        pion[valeur] = ["images/"+type_pion[j]+color[i]+".png", nombre_pion[j]]
    info_pion[color[i]] = pion

print(info_pion)


def lancee_jeu(info_pion):

    pygame.init()

    pygame.display.set_caption("jeu echecs")
    fenetre = pygame.display.set_mode((1000, 1000))

    partie = Partie(info_pion)

    lancée = True
    finie = False

    while lancée:

        partie.groupe_pion.draw(fenetre)

        pygame.display.flip()

        for event in pygame.event.get():

            for i in range(dificulter):
                if not partie.decouvert[i]:
                    finie = False
                    break
                finie = True
            if finie:
                lancée = False

            if event.type == pygame.QUIT:
                lancée = False
                pygame.quit()


            elif event.type == pygame.MOUSEBUTTONUP:
                p = pygame.mouse.get_pos()
                for carte in partie.groupe_carte:
                    if carte.rect.collidepoint(p[0], p[1]) and event.button == 1:
                        if not carte.afficher:
                            partie.Verif(carte)
                            carte.Afficher()
                        else:
                            if not partie.decouvert[carte.paire] and partie.retourner[0] != carte.paire:
                                carte.Cacher()

    pygame.quit()
    if finie:
        print("Vous avez gagné ! Félicitations !")


while True:
    rejouet = str(input("Voulez vous jouer (OUI/NON) :"))
    if rejouet.upper() == "OUI":
        lancee_jeu(info_pion)
    else:
        break
