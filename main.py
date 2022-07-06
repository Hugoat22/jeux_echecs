import pygame

info_pion = {}
color = ["blanc", "noir"]

for i in range(2):
    pion = {"soldat": ["images/soldat" + color[i] + ".png", 8], "tour": ["images/soldat" + color[i] + ".png", 8]}
    info_pion[color[i]] = pion

print(info_pion)


def lancee_jeu(liste_image):
    while True:
        dificulter = int(input("La difficulté va de 1 à 8. Nombre indisponible (7). Niveau recommandé (8):"))
        if dificulter != 7:
            break
        else:
            print("Veuillez renseigner une valeur valable !")

    pygame.init()

    pygame.display.set_caption("Memo Melo")
    fenetre = pygame.display.set_mode((1000, 1000))

    partie = Partie(dificulter, liste_image)

    lancée = True
    finie = False

    while lancée:

        partie.groupe_carte.draw(fenetre)

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
        lancee_jeu(liste_image)
    else:
        break
