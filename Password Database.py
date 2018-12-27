def IpDatabase():
    try:
        import pygame
    except ImportError:
        print("pygame is required to run this application. Visit https://www.pygame.org/wiki/GettingStarted")

    import random, os, datetime, re

    pygame.init()

    red = (255,0,0)
    darkRed = (180,0,0)
    green = (0,255,0)
    lightGreen = (42,201,26)
    darkGreen = (22,162,8)
    orange = (238,143,0)
    darkOrange = (206,126,7)
    blue = (0,0,255)
    darkBlue = (0,0,128)
    white = (255,255,255)
    darkWhite = (196,196,196)
    black = (0,0,0)
    pink = (255,200,200)
    grey = (45,45,45)
    lightGrey = (91,91,91)
    darkGrey = (23,23,23)
    brown = (54,42,24)

    clock = pygame.time.Clock()

    smallText = pygame.font.SysFont(None, 20)
    largeText = pygame.font.SysFont(None, 60)
    menuText = pygame.font.Font("fonts\Sony_Sketch_EF.ttf", 60)

    videoSettings = True
    settingsWidthOpen = False
    settingsFullscreen = False
    fullscreen = True
    app = False
    settingsWidthText = smallText.render("Width/Height: ", True, black)
    settingsWidthOptionText1 = smallText.render("1600x800", True, black)
    settingsWidthOptionText2 = smallText.render("1200x600", True, black)
    settingsWidthOptionText3 = smallText.render("800x400", True, black)
    settingsFullscreenText = smallText.render("Fullscreen:", True, black)
    settingsFullscreenOptionText = smallText.render("X", True, green)
    settingsWidthBox = pygame.Rect(20, 50, settingsWidthText.get_rect().width+5, 20)
    settingsWidthOptions1 = pygame.Rect(140, 50, 100, 20)
    settingsWidthOptions2 = pygame.Rect(140, 80, 100, 20)
    settingsWidthOptions3 = pygame.Rect(140, 110, 100, 20)
    settingsWidthConfirmBox = pygame.Rect(250, 50, 20, 20)
    settingsFullscreenBox = pygame.Rect(100, 150, 20, 20)
    settingsConfirmBox = pygame.Rect(300, 150, 70, 20)

    display = pygame.display.set_mode((400,200))
    pygame.display.set_caption("Video Settings")

    pygame.display.set_icon(pygame.image.load("images\greyhackpdb-logo.png"))
    
    while videoSettings:
        display.fill(white)

        pygame.draw.rect(display, black, settingsFullscreenBox)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = event.pos
                if settingsWidthBox.collidepoint(mousePos):
                    if not settingsWidthOpen:
                        settingsWidthOpen = True
                    else:
                        settingsWidthOpen = False
                if settingsFullscreenBox.collidepoint(mousePos):
                    if not fullscreen:
                        fullscreen = True
                    else:
                        fullscreen = False
                if settingsWidthOptions1.collidepoint(mousePos) and settingsWidthOpen:
                    settingsWidthConfirmBox.y = 50
                if settingsWidthOptions2.collidepoint(mousePos) and settingsWidthOpen:
                    settingsWidthConfirmBox.y = 80
                if settingsWidthOptions3.collidepoint(mousePos) and settingsWidthOpen:
                    settingsWidthConfirmBox.y = 110
                if settingsConfirmBox.collidepoint(mousePos):
                    app = True
                        
            if event.type == pygame.MOUSEMOTION:
                mousePos = event.pos

        if settingsWidthBox.collidepoint(mousePos):
            pygame.draw.rect(display, darkWhite, settingsWidthBox)
        else:
            pygame.draw.rect(display, lightGrey, settingsWidthBox)
        if settingsConfirmBox.collidepoint(mousePos):
            pygame.draw.rect(display, darkWhite, settingsConfirmBox)
            settingsConfirmText = smallText.render("Confirm", True, darkGreen)
        else:
            pygame.draw.rect(display, lightGrey, settingsConfirmBox)
            settingsConfirmText = smallText.render("Confirm", True, green)

        if fullscreen:
            display.blit(settingsFullscreenOptionText, (105, 155))

        if settingsWidthOpen:
            if settingsWidthOptions1.collidepoint(mousePos):
                pygame.draw.rect(display, darkWhite, settingsWidthOptions1)
            else:
                pygame.draw.rect(display, lightGrey, settingsWidthOptions1)
            if settingsWidthOptions2.collidepoint(mousePos):
                pygame.draw.rect(display, darkWhite, settingsWidthOptions2)
            else:
                pygame.draw.rect(display, lightGrey, settingsWidthOptions2)
            if settingsWidthOptions3.collidepoint(mousePos):
                pygame.draw.rect(display, darkWhite, settingsWidthOptions3)
            else:
                pygame.draw.rect(display, lightGrey, settingsWidthOptions3)
            display.blit(settingsWidthOptionText1, (145, 55))
            display.blit(settingsWidthOptionText2, (145, 85))
            display.blit(settingsWidthOptionText3, (145, 115))

        display.blit(settingsWidthText, (25, 55))
        display.blit(settingsFullscreenText, (25, 155))
        display.blit(settingsConfirmText, (310, 153))

        if settingsWidthOpen and not fullscreen:
            pygame.draw.rect(display, black, settingsWidthConfirmBox)
            display.blit(settingsFullscreenOptionText, (settingsWidthConfirmBox.x+5, settingsWidthConfirmBox.y+3))

        if app:
            if not fullscreen:
                if settingsWidthConfirmBox.y == 50:
                    displayWidth = 1600
                    displayHeight = 800
                if settingsWidthConfirmBox.y == 80:
                    displayWidth = 1200
                    displayHeight = 600
                if settingsWidthConfirmBox.y == 110:
                    displayWidth = 800
                    displayHeight = 400
            pygame.display.quit()
            break
        
        pygame.display.update()
        clock.tick(60)

    os.environ["SDL_VIDEO_CENTERED"] = "1"

    pygame.display.init()

    if not fullscreen:
        display = pygame.display.set_mode((displayWidth, displayHeight))
    else:
        display = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        displayWidth = pygame.display.Info().current_w
        displayHeight = pygame.display.Info().current_h
    pygame.display.set_caption("GreyHack Password Database")
    pygame.display.set_icon(pygame.image.load("images\greyhackpdb-logo.png"))
    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
    
    menuSearchBox = pygame.Rect(displayWidth*0.35, displayHeight*0.2, displayWidth*0.3, displayHeight*0.1)
    menuAddBox = pygame.Rect(displayWidth*0.35, displayHeight*0.35, displayWidth*0.3, displayHeight*0.1)
    menuDatabaseBox = pygame.Rect(displayWidth*0.35, displayHeight*0.5, displayWidth*0.3, displayHeight*0.1)
    menuQuitBox = pygame.Rect(displayWidth*0.35, displayHeight*0.75, displayWidth*0.3, displayHeight*0.1)
    menuAddOptionsBox1 = pygame.Rect(displayWidth*0.7, displayHeight*0.35, displayWidth*0.2, displayHeight*0.1)
    menuAddOptionsBox2 = pygame.Rect(displayWidth*0.7, displayHeight*0.5, displayWidth*0.2, displayHeight*0.1)
    menuAddOptionsBox3 = pygame.Rect(displayWidth*0.7, displayHeight*0.65, displayWidth*0.2, displayHeight*0.1)
    menuDatabaseOptionsBox1 = pygame.Rect(displayWidth*0.1, displayHeight*0.5, displayWidth*0.2, displayHeight*0.1)
    menuDatabaseOptionsBox2 = pygame.Rect(displayWidth*0.1, displayHeight*0.65, displayWidth*0.2, displayHeight*0.1)
    menuDatabaseOptionsBox3 = pygame.Rect(displayWidth*0.1, displayHeight*0.8, displayWidth*0.2, displayHeight*0.1)
    searchInputBox = pygame.Rect(displayWidth*0.2, displayHeight*0.4, displayWidth*0.6, displayHeight*0.2)
    resultsDeleteBox = pygame.Rect(displayWidth*0.4, displayHeight*0.9, displayWidth*0.2, displayHeight*0.05)
    returnMenuBox = pygame.Rect(displayWidth*0.83, displayHeight*0.05, displayWidth*0.12, displayHeight*0.1)
    addServerConfirmBox = pygame.Rect(displayWidth*0.4, displayHeight*0.85, displayWidth*0.2, displayHeight*0.1)
    databaseHeaderBox = pygame.Rect(displayWidth*0.2, displayHeight*0.05, displayWidth*0.6, displayHeight*0.1)
    databaseIpBox = pygame.Rect(displayWidth*0.2, databaseHeaderBox.y + databaseHeaderBox.height, displayWidth*0.6, displayHeight*0.1)

    size = 70
    smallText = pygame.font.SysFont(None, 30)

    if displayWidth <= 1000 and displayHeight <= 500:
        circle1 = pygame.image.load("images\small-loading-circle1.png")
        circle2 = pygame.image.load("images\small-loading-circle2.png")
        circle3 = pygame.image.load("images\small-loading-circle3.png")
        circle4 = pygame.image.load("images\small-loading-circle4.png")
        circle5 = pygame.image.load("images\small-loading-circle5.png")
        circle6 = pygame.image.load("images\small-loading-circle6.png")
        circle7 = pygame.image.load("images\small-loading-circle7.png")
        circle8 = pygame.image.load("images\small-loading-circle8.png")
        largeText = pygame.font.SysFont(None, 40)
        spaceText = pygame.font.Font("fonts\space age.ttf", 25)
        menuText = pygame.font.Font("fonts\Sony_Sketch_EF.ttf", 40)
        smallText = pygame.font.SysFont(None, 20)
        size = 40
        smallerText = True
    else:
        circle1 = pygame.image.load("images\loading-circle1.png")
        circle2 = pygame.image.load("images\loading-circle2.png")
        circle3 = pygame.image.load("images\loading-circle3.png")
        circle4 = pygame.image.load("images\loading-circle4.png")
        circle5 = pygame.image.load("images\loading-circle5.png")
        circle6 = pygame.image.load("images\loading-circle6.png")
        circle7 = pygame.image.load("images\loading-circle7.png")
        circle8 = pygame.image.load("images\loading-circle8.png")
        smallerText = False

    greyHackImg = pygame.image.load("images\greyhack.png")

    addServerConfirmText = largeText.render("Confirm", True, black)
    menuSearchText = menuText.render("Search", True, black)
    menuAddText = menuText.render("Add", True, black)
    menuDatabaseText = menuText.render("Database", True, black)
    menuQuitText = menuText.render("Exit", True, black)
    menuAddOptionsText1 = menuText.render("Server", True, black)
    menuAddOptionsText2 = menuText.render("Email", True, black)
    menuAddOptionsText3 = menuText.render("Bank", True, black)
    menuDatabaseOptionsText1 = menuText.render("Server", True, black)
    menuDatabaseOptionsText2 = menuText.render("Email", True, black)
    menuDatabaseOptionsText3 = menuText.render("Bank", True, black)
    returnMenuText = largeText.render("Menu", True, black)
    searchErrorText = largeText.render("Invalid field", True, red)
    resultsDeleteText = smallText.render("Delete", True, black)
    addServerErrorText = smallText.render("Missing paramaters", True, red)
    addBankErrorText = largeText.render("Missing fields", True, red)

    opening = True
    menu = False
    search = False
    loading = False
    results = False
    addServer = False
    addServerLoading = False
    viewDatabase = False
    exit = False
    searchError = False
    addServerError = False
    addEmail = False
    addBank = False
    menuAddOptions = False
    menuDatabaseOptions = False
    addEmail = False
    addEmailError = False
    addEmailLoading = False
    addBank = False
    addBankLoading = False
    addBankError = False

    pattern = r"^[0-9]*[0-9]$"

    usernameDict = {}
    passwordDict = {}
    sudoDict = {}
    emailDict = {}
    bankDict = {}

    r = 255
    g = 255
    b = 255

    pygame.scrap.init()

    with open("resources\\usernameDB.txt") as f:
        for line in f.readlines():
            if line[-1] == "\n":
                usernameDict[line[1:line.index(":")]] = line[line.index(":")+1:-2]
            else:
                usernameDict[line[1:line.index(":")]] = line[line.index(":")+1:-1]
        f.close()
    with open("resources\passwordDB.txt") as f:
        for line in f.readlines():
            if line[-1] == "\n":
                passwordDict[line[1:line.index(":")]] = line[line.index(":")+1:-2]
            else:
                passwordDict[line[1:line.index(":")]] = line[line.index(":")+1:-1]
        f.close()
    with open("resources\sudoDB.txt") as f:
        for line in f.readlines():
            if line[-1] == "\n":
                sudoDict[line[1:line.index(":")]] = line[line.index(":")+1:-2]
            else:
                sudoDict[line[1:line.index(":")]] = line[line.index(":")+1:-1]
        f.close()
    with open("resources\emailDB.txt") as f:
        for line in f.readlines():
            if line[-1] == "\n":
                emailDict[line[1:line.index(":")]] = line[line.index(":")+1:-2]
            else:
                emailDict[line[1:line.index(":")]] = line[line.index(":")+1:-1]
        f.close()
    with open("resources\\bankDB.txt") as f:
        for line in f.readlines():
            if line[-1] == "\n":
                bankDict[line[1:line.index(":")]] = line[line.index(":")+1:-2]
            else:
                bankDict[line[1:line.index(":")]] = line[line.index(":")+1:-1]
        f.close()
    
    def CenterText(surface, text):
        return (surface.x + surface.width*0.5 - text.get_rect().width*0.5, surface.y + surface.height*0.5 - text.get_rect().height*0.5)

    def AddText(event, string, special=None):
        if special == "ip" or special == "number":
            if event.key in range(48, 58):
                if (special == "ip" and event.key == 48) and (string == "" or string != "" and string[-1] == "."):
                    return string
                else:
                    string += event.unicode
            if event.key == pygame.K_BACKSPACE:
                string = string[:-1]
            if event.key == 46 and special != "number":
                string += event.unicode
            return string
        if event.key == pygame.K_BACKSPACE:
            string = string[:-1]
        elif event.key != 59 and event.key != pygame.K_ESCAPE:
            string += event.unicode
        return string
                   
    while not exit:
            
        while opening:
            
            display.fill((r,g,b))

            if r != 0:
                r -= 1
                g -= 1
                b -= 1
            else:
                spaceText = pygame.font.Font("fonts\space age.ttf", size)
                openingText = spaceText.render("GreyHack Password Database", True, red)
                display.blit(openingText, (displayWidth*0.5 - openingText.get_rect().width*0.5, displayHeight*0.5 - openingText.get_rect().height*0.5))
                if not smallerText:
                    if size == 51:
                        start = datetime.datetime.now().second
                        if start == 54:
                            start = -6
                        if start == 55:
                            start = -5
                        if start == 56:
                            start = -4
                        if start == 57:
                            start = -3
                        if start == 58:
                            start = -2
                        if start == 59:
                            start = -1
                    if size > 50:
                        size -= 1
                    if size == 50:
                        end = datetime.datetime.now().second
                        if end == start + 6:
                            opening = False
                            menu = True
                else:
                    if size == 26:
                        start = datetime.datetime.now().second
                        if start == 54:
                            start = -6
                        if start == 55:
                            start = -5
                        if start == 56:
                            start = -4
                        if start == 57:
                            start = -3
                        if start == 58:
                            start = -2
                        if start == 59:
                            start = -1
                    if size > 25:
                        size -= 1
                    if size == 25:
                        end = datetime.datetime.now().second
                        if end == start + 6:
                            opening = False
                            menu = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            pygame.display.update()
            clock.tick(60)

        while menu:

            display.fill(lightGrey)
            display.blit(pygame.transform.scale(greyHackImg, (displayWidth, displayHeight)), (0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEMOTION:
                    mousePos = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = event.pos
                    if menuSearchBox.collidepoint(mousePos):
                        menu = False
                        search = True
                        searchError = False
                        menuAddOptions = False
                        menuDatabaseOptions = False
                        returnMenuBox.x = displayWidth*0.83
                        inputTextString = ""
                        inputTextStringDisp = ""
                        resultOption = 0
                        resultsDeleteShow = False
                    if menuAddBox.collidepoint(mousePos):
                        if not menuAddOptions:
                            menuAddOptions = True
                        else:
                            menuAddOptions = False
                    if menuDatabaseBox.collidepoint(mousePos):
                        if not menuDatabaseOptions:
                            menuDatabaseOptions = True
                        else:
                            menuDatabaseOptions = False
                    if menuQuitBox.collidepoint(mousePos):
                        pygame.quit()
                        quit()
                    if menuAddOptions:
                        if menuAddOptionsBox1.collidepoint(mousePos):
                            menu = False
                            addServer = True
                            addServerError = False
                            addServerLoading = False
                            menuAddOptions = False
                            menuDatabaseOptions = False
                            returnMenuBox.x = displayWidth*0.83
                            inputTextStringIp = ""
                            inputTextStringUsername = ""
                            inputTextStringPassword = ""
                            inputTextStringSudo = ""
                            inputTextString = ""
                            inputTextStringDisp = ""
                            focus = 1
                        if menuAddOptionsBox2.collidepoint(mousePos):
                            menu = False
                            addEmail = True
                            addEmailError = False
                            addEmailLoading = False
                            menuAddOptions = False
                            menuDatabaseOptions = False
                            returnMenuBox.x = displayWidth*0.83
                            emailInputTextString = ""
                            emailPasswordInputTextString = ""
                            focus = 1
                        if menuAddOptionsBox3.collidepoint(mousePos):
                            menu = False
                            addBank = True
                            addBankError = False
                            addBankLoading = False
                            menuAddOptions = False
                            menuDatabaseOptions = False
                            returnMenuBox.x = displayWidth*0.83
                            addBankNumberInputTextString = ""
                            addBankPasswordInputTextString = ""
                            focus = 1
                    if menuDatabaseOptions:
                        if menuDatabaseOptionsBox1.collidepoint(mousePos):
                            menu = False
                            viewDatabase = True
                            menuAddOptions = False
                            menuDatabaseOptions = False
                            databaseHeaderText = largeText.render("IP", True, black)
                            returnMenuBox.x = displayWidth*0.87
                            databaseIpList = []
                            for ip in usernameDict:
                                databaseIpList.append(ip)
                            for ip in passwordDict:
                                if ip not in databaseIpList:
                                    databaseIpList.append(ip)
                            for ip in sudoDict:
                                if ip not in databaseIpList:
                                    databaseIpList.append(ip)
                            if len(databaseIpList) == 0:
                                databaseIpList.append("No IPs in database")
                            i = 10
                        if menuDatabaseOptionsBox2.collidepoint(mousePos):
                            menu = False
                            viewDatabase = True
                            menuAddOptions = False
                            menuDatabaseOptions = False
                            databaseHeaderText = largeText.render("Email", True, black)
                            returnMenuBox.x = displayWidth*0.87
                            databaseIpList = []
                            for email in emailDict:
                                databaseIpList.append(email)
                            if len(databaseIpList) == 0:
                                databaseIpList.append("No emails in database")
                            i = 10
                        if menuDatabaseOptionsBox3.collidepoint(mousePos):
                            menu = False
                            viewDatabase = True
                            menuAddOptions = False
                            menuDatabaseOptions = False
                            databaseHeaderText = largeText.render("Account Number", True, black)
                            returnMenuBox.x = displayWidth*0.87
                            databaseIpList = []
                            for accountNumber in bankDict:
                                databaseIpList.append(accountNumber)
                            if len(databaseIpList) == 0:
                                databaseIpList.append("No accounts in database")
                            i = 10

            if menuSearchBox.collidepoint(mousePos):
                pygame.draw.rect(display, orange, menuSearchBox)
            else:
                pygame.draw.rect(display, darkOrange, menuSearchBox)
            if menuAddBox.collidepoint(mousePos):
                pygame.draw.rect(display, orange, menuAddBox)
            else:
                pygame.draw.rect(display, darkOrange, menuAddBox)
            if menuDatabaseBox.collidepoint(mousePos):
                pygame.draw.rect(display, orange, menuDatabaseBox)
            else:
                pygame.draw.rect(display, darkOrange, menuDatabaseBox)
            if menuQuitBox.collidepoint(mousePos):
                pygame.draw.rect(display, red, menuQuitBox)
            else:
                pygame.draw.rect(display, darkRed, menuQuitBox)
            if menuAddOptions:
                if menuAddOptionsBox1.collidepoint(mousePos):
                    pygame.draw.rect(display, orange, menuAddOptionsBox1)
                else:
                    pygame.draw.rect(display, darkOrange, menuAddOptionsBox1)
                if menuAddOptionsBox2.collidepoint(mousePos):
                    pygame.draw.rect(display, orange, menuAddOptionsBox2)
                else:
                    pygame.draw.rect(display, darkOrange, menuAddOptionsBox2)
                if menuAddOptionsBox3.collidepoint(mousePos):
                    pygame.draw.rect(display, orange, menuAddOptionsBox3)
                else:
                    pygame.draw.rect(display, darkOrange, menuAddOptionsBox3)
                display.blit(menuAddOptionsText1, CenterText(menuAddOptionsBox1, menuAddOptionsText1))
                display.blit(menuAddOptionsText2, CenterText(menuAddOptionsBox2, menuAddOptionsText2))
                display.blit(menuAddOptionsText3, CenterText(menuAddOptionsBox3, menuAddOptionsText3))
            if menuDatabaseOptions:
                if menuDatabaseOptionsBox1.collidepoint(mousePos):
                    pygame.draw.rect(display, orange, menuDatabaseOptionsBox1)
                else:
                    pygame.draw.rect(display, darkOrange, menuDatabaseOptionsBox1)
                if menuDatabaseOptionsBox2.collidepoint(mousePos):
                    pygame.draw.rect(display, orange, menuDatabaseOptionsBox2)
                else:
                    pygame.draw.rect(display, darkOrange, menuDatabaseOptionsBox2)
                if menuDatabaseOptionsBox3.collidepoint(mousePos):
                    pygame.draw.rect(display, orange, menuDatabaseOptionsBox3)
                else:
                    pygame.draw.rect(display, darkOrange, menuDatabaseOptionsBox3)
                display.blit(menuDatabaseOptionsText1, CenterText(menuDatabaseOptionsBox1, menuDatabaseOptionsText1))
                display.blit(menuDatabaseOptionsText2, CenterText(menuDatabaseOptionsBox2, menuDatabaseOptionsText2))
                display.blit(menuDatabaseOptionsText3, CenterText(menuDatabaseOptionsBox3, menuDatabaseOptionsText3))

            addServerLoading = False

            display.blit(menuSearchText, CenterText(menuSearchBox, menuSearchText))
            display.blit(menuAddText, CenterText(menuAddBox, menuAddText))
            display.blit(menuDatabaseText, CenterText(menuDatabaseBox, menuDatabaseText))
            display.blit(menuQuitText, CenterText(menuQuitBox, menuQuitText))
            
            pygame.display.update()
            clock.tick(60)
            
        while search:
                
            display.fill(black)

            searchInputBox.y = displayHeight*0.4
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key != pygame.K_RETURN:
                        inputTextString = AddText(event, inputTextString)
                    if event.key == pygame.K_ESCAPE:
                        search = False
                        menu = True
                    if event.key == pygame.K_RETURN:
                        if len(inputTextString) > 0:
                            if inputTextString.count(".") == 3:
                                inputIp1 = inputTextStringDisp[:inputTextStringDisp.find(".")]
                                inputTextStringDisp = inputTextStringDisp[inputTextStringDisp.find(".")+1:]
                                inputIp2 = inputTextStringDisp[:inputTextStringDisp.find(".")]
                                inputTextStringDisp = inputTextStringDisp[inputTextStringDisp.find(".")+1:]
                                inputIp3 = inputTextStringDisp[:inputTextStringDisp.find(".")]
                                inputTextStringDisp = inputTextStringDisp[inputTextStringDisp.find(".")+1:]
                                inputIp4 = inputTextStringDisp
                                if int(inputIp1) <= 255 and int(inputIp2) <= 255 and int(inputIp3) <= 255 and int(inputIp4) <= 255:
                                    resultOption = 1
                                    resultsDeleteBox.y = displayHeight*0.9
                            if resultOption != 1:
                                try:
                                    inputTextString.index("@")
                                except ValueError:
                                    if re.match(pattern, inputTextString):
                                        resultOption = 3
                                        resultsDeleteBox.y = displayHeight*0.6
                                else:
                                    resultOption = 2
                                    resultsDeleteBox.y = displayHeight*0.6
                        else:
                            searchError = True
                        if resultOption in range(1, 4):
                            search = False
                            loading = True
                            loadingCircle1 = True
                            loadingCircle2 = False
                            loadingCircle3 = False
                            loadingCircle4 = False
                            loadingCircle5 = False
                            loadingCircle6 = False
                            loadingCircle7 = False
                            loadingCircle8 = False
                            cycle = 0
                            start = datetime.datetime.now().second
                if event.type == pygame.MOUSEMOTION:
                    mousePos = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = event.pos
                    if returnMenuBox.collidepoint(mousePos):
                        search = False
                        menu = True

            if searchInputBox.collidepoint(mousePos):
                pygame.draw.rect(display, lightGrey, searchInputBox)
            else:
                pygame.draw.rect(display, grey, searchInputBox)
            if returnMenuBox.collidepoint(mousePos):
                pygame.draw.rect(display, lightGrey, returnMenuBox)
            else:
                pygame.draw.rect(display, grey, returnMenuBox)

            inputTextStringDisp = inputTextString
            
            inputText = largeText.render(inputTextString, True, white)

            if searchError:
                display.blit(searchErrorText, (displayWidth*0.5 - searchErrorText.get_rect().width*0.5, displayHeight*0.8))

            display.blit(inputText, CenterText(searchInputBox, inputText))
            display.blit(returnMenuText, CenterText(returnMenuBox, returnMenuText))

            pygame.display.update()
            clock.tick(60)

        while loading:
                
            display.fill(black)

            end = datetime.datetime.now().second

            if start == 59:
                start = -1

            searchInputBox.y = displayHeight*0.1
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEMOTION:
                    mousePos = event.pos

            if not addServerLoading and not addEmailLoading and not addBankLoading:
                if searchInputBox.collidepoint(mousePos):
                    pygame.draw.rect(display, grey, searchInputBox)
                else:
                    pygame.draw.rect(display, darkGrey, searchInputBox)

            if cycle == 2:
                if addServerLoading or addEmailLoading or addBankLoading:
                    display.blit(circle1, (displayWidth*0.4, displayHeight*0.35))
                else:
                    display.blit(circle1, (displayWidth*0.4, displayHeight*0.45))
                if end == start + 1 and not addServerLoading and not addEmailLoading and not addBankLoading:
                    loading = False
                    results = True
                    if resultOption == 1:
                        if inputTextString in usernameDict:
                            usernameText = largeText.render("Username: {}".format(usernameDict[inputTextString]), True, white)
                        else:
                            usernameText = largeText.render("Username: Username not found", True, red)
                        if inputTextString in passwordDict:
                            passwordText = largeText.render("Password: {}".format(passwordDict[inputTextString]), True, white)
                        else:
                            passwordText = largeText.render("Password: Password not found", True, red)
                        if inputTextString in sudoDict:
                            sudoText = largeText.render("Sudo: {}".format(sudoDict[inputTextString]), True, white)
                        else:
                            sudoText = largeText.render("Sudo: Sudo key not found", True, red)
                        if inputTextString in usernameDict or inputTextString in passwordDict or inputTextString in sudoDict:
                            resultsDeleteShow = True
                        break
                    if resultOption == 2:
                        if inputTextString in emailDict:
                            usernameText = largeText.render("Password: {}".format(emailDict[inputTextString]), True, white)
                            resultsDeleteShow = True
                        else:
                            usernameText = largeText.render("Password: Password not found", True, red)
                            break
                    if resultOption == 3:
                        if inputTextString in bankDict:
                            usernameText = largeText.render("Password: {}".format(bankDict[inputTextString]), True, white)
                            resultsDeleteShow = True
                        else:
                            usernameText = largeText.render("Password: Password not found", True, red)
                            break
                if end == start + 1 and addServerLoading:
                    with open("resources\\usernameDB.txt", "a") as f:
                        if len(usernameDict) == 0:
                            f.write("\"{}:{}\"".format(inputTextStringIp, inputTextStringUsername))
                        else:
                            f.write("\n\"{}:{}\"".format(inputTextStringIp, inputTextStringUsername))
                        f.close()
                    with open("resources\passwordDB.txt", "a") as f:
                        if len(passwordDict) == 0:
                            f.write("\"{}:{}\"".format(inputTextStringIp, inputTextStringPassword))
                        else:
                            f.write("\n\"{}:{}\"".format(inputTextStringIp, inputTextStringPassword))
                        f.close()
                    with open("resources\sudoDB.txt", "a") as f:
                        if len(sudoDict) == 0:
                            f.write("\"{}:{}\"".format(inputTextStringIp, inputTextStringSudo))
                        else:
                            f.write("\n\"{}:{}\"".format(inputTextStringIp, inputTextStringSudo))
                        f.close()
                    usernameDict[inputTextStringIp] = inputTextStringUsername
                    passwordDict[inputTextStringIp] = inputTextStringPassword
                    sudoDict[inputTextStringIp] = inputTextStringSudo
                    loading = False
                    addServerLoading = False
                    menu = True
                    break
                if end == start + 1 and addEmailLoading:
                    with open("resources\emailDB.txt", "a") as f:
                        if len(emailDict) == 0:
                            f.write("\"{}:{}\"".format(emailInputTextString, emailPasswordInputTextString))
                        else:
                            f.write("\n\"{}:{}\"".format(emailInputTextString, emailPasswordInputTextString))
                        f.close()
                    emailDict[emailInputTextString] = emailPasswordInputTextString
                    loading = False
                    addEmailLoading = False
                    menu = True
                    break
                if end == start + 1 and addBankLoading:
                    with open("resources\\bankDB.txt", "a") as f:
                        if len(bankDict) == 0:
                            f.write("\"{}:{}\"".format(addBankNumberInputTextString, addBankPasswordInputTextString))
                        else:
                            f.write("\n\"{}:{}\"".format(addBankNumberInputTextString, addBankPasswordInputTextString))
                        f.close()
                    bankDict[addBankNumberInputTextString] = addBankPasswordInputTextString
                    loading = False
                    addBankLoading = False
                    menu = True
                    break
                
            if loadingCircle1:
                if addServerLoading or addEmailLoading or addBankLoading:
                    display.blit(circle1, (displayWidth*0.4, displayHeight*0.35))
                else:
                    display.blit(circle1, (displayWidth*0.4, displayHeight*0.45))
                if end == start + 1:
                    start = datetime.datetime.now().second
                    loadingCircle1 = False
                    loadingCircle2 = True
                    cycle += 1
            if loadingCircle2:
                if addServerLoading or addEmailLoading or addBankLoading:
                    display.blit(circle2, (displayWidth*0.4, displayHeight*0.35))
                else:
                    display.blit(circle2, (displayWidth*0.4, displayHeight*0.45))
                if end == start + 1:
                    start = datetime.datetime.now().second
                    loadingCircle2 = False
                    loadingCircle3 = True
            if loadingCircle3:
                if addServerLoading or addEmailLoading or addBankLoading:
                    display.blit(circle3, (displayWidth*0.4, displayHeight*0.35))
                else:
                    display.blit(circle3, (displayWidth*0.4, displayHeight*0.45))
                if end == start + 1:
                    start = datetime.datetime.now().second
                    loadingCircle3 = False
                    loadingCircle4 = True
            if loadingCircle4:
                if addServerLoading or addEmailLoading or addBankLoading:
                    display.blit(circle4, (displayWidth*0.4, displayHeight*0.35))
                else:
                    display.blit(circle4, (displayWidth*0.4, displayHeight*0.45))
                if end == start + 1:
                    start = datetime.datetime.now().second
                    loadingCircle4 = False
                    loadingCircle5 = True
            if loadingCircle5:
                if addServerLoading or addEmailLoading or addBankLoading:
                    display.blit(circle5, (displayWidth*0.4, displayHeight*0.35))
                else:
                    display.blit(circle5, (displayWidth*0.4, displayHeight*0.45))
                if end == start + 1:
                    start = datetime.datetime.now().second
                    loadingCircle5 = False
                    loadingCircle6 = True
            if loadingCircle6:
                if addServerLoading or addEmailLoading or addBankLoading:
                    display.blit(circle6, (displayWidth*0.4, displayHeight*0.35))
                else:
                    display.blit(circle6, (displayWidth*0.4, displayHeight*0.45))
                if end == start + 1:
                    start = datetime.datetime.now().second
                    loadingCircle6 = False
                    loadingCircle7 = True
            if loadingCircle7:
                if addServerLoading or addEmailLoading or addBankLoading:
                    display.blit(circle7, (displayWidth*0.4, displayHeight*0.35))
                else:
                    display.blit(circle7, (displayWidth*0.4, displayHeight*0.45))
                if end == start + 1:
                    start = datetime.datetime.now().second
                    loadingCircle7 = False
                    loadingCircle8 = True
            if loadingCircle8:
                if addServerLoading or addEmailLoading or addBankLoading:
                    display.blit(circle8, (displayWidth*0.4, displayHeight*0.35))
                else:
                    display.blit(circle8, (displayWidth*0.4, displayHeight*0.45))
                if end == start + 1:
                    start = datetime.datetime.now().second
                    loadingCircle8 = False
                    loadingCircle1 = True

            if not addServerLoading and not addEmailLoading and not addBankLoading:
                inputText = largeText.render(inputTextString, True, darkWhite)
                display.blit(inputText, CenterText(searchInputBox, inputText))

            pygame.display.update()
            clock.tick(60)

        while results:
                
            display.fill(black)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        results = False
                        menu = True
                if event.type == pygame.MOUSEMOTION:
                    mousePos = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = event.pos
                    if returnMenuBox.collidepoint(mousePos):
                        results = False
                        menu = True
                    if searchInputBox.collidepoint(mousePos):
                        pygame.scrap.put(pygame.SCRAP_TEXT, pygame.compat.as_bytes(inputTextString))
                    if usernameBox.collidepoint(mousePos):
                        if resultOption == 1:
                            if inputTextString in usernameDict:
                                pygame.scrap.put(pygame.SCRAP_TEXT, pygame.compat.as_bytes(usernameDict[inputTextString]))
                        if resultOption == 2:
                            if inputTextString in emailDict:
                                pygame.scrap.put(pygame.SCRAP_TEXT, pygame.compat.as_bytes(emailDict[inputTextString]))
                        if resultOption == 3:
                            if inputTextString in bankDict:
                                pygame.scrap.put(pygame.SCRAP_TEXT, pygame.compat.as_bytes(bankDict[inputTextString]))
                    if resultOption == 1 and passwordBox.collidepoint(mousePos):
                        if inputTextString in passwordDict:
                            pygame.scrap.put(pygame.SCRAP_TEXT, pygame.compat.as_bytes(passwordDict[inputTextString]))
                    if resultOption == 1 and sudoBox.collidepoint(mousePos):
                        if inputTextString in sudoDict:
                            pygame.scrap.put(pygame.SCRAP_TEXT, pygame.compat.as_bytes(sudoDict[inputTextString]))
                    if resultsDeleteShow and resultsDeleteBox.collidepoint(mousePos):
                        if resultOption == 1:
                            if inputTextString in usernameDict:
                                usernameDict.pop(inputTextString)
                            if inputTextString in passwordDict:
                                passwordDict.pop(inputTextString)
                            if inputTextString in sudoDict:
                                sudoDict.pop(inputTextString)
                            with open("resources\\usernameDB.txt", "w") as f:
                                for key in usernameDict:
                                    if key == list(usernameDict.keys())[0]:
                                        f.write("\"{}:{}\"".format(key, usernameDict[key]))
                                    else:
                                        f.write("\n\"{}:{}\"".format(key, usernameDict[key]))
                                f.close()
                            with open("resources\passwordDB.txt", "w") as f:
                                for key in passwordDict:
                                    if key == list(passwordDict.keys())[0]:
                                        f.write("\"{}:{}\"".format(key, passwordDict[key]))
                                    else:
                                        f.write("\n\"{}:{}\"".format(key, passwordDict[key]))
                                f.close()
                            with open("resources\sudoDB.txt", "w") as f:
                                for key in sudoDict:
                                    if key == list(sudoDict.keys())[0]:
                                        f.write("\"{}:{}\"".format(key, sudoDict[key]))
                                    else:
                                        f.write("\n\"{}:{}\"".format(key, sudoDict[key]))
                                f.close()
                        if resultOption == 2:
                            emailDict.pop(inputTextString)
                            with open("resources\emailDB.txt", "w") as f:
                                for key in emailDict:
                                    if key == list(emailDict.keys())[0]:
                                        f.write("\"{}:{}\"".format(key, emailDict[key]))
                                    else:
                                        f.write("\n\"{}:{}\"".format(key, emailDict[key]))
                                f.close()
                        if resultOption == 3:
                            bankDict.pop(inputTextString)
                            with open("resources\\bankDB.txt", "w") as f:
                                for key in bankDict:
                                    if key == list(bankDict.keys())[0]:
                                        f.write("\"{}:{}\"".format(key, bankDict[key]))
                                    else:
                                        f.write("\n\"{}:{}\"".format(key, bankDict[key]))
                                f.close()
                        results = False
                        menu = True

            usernameBox = pygame.Rect(displayWidth*0.5 - usernameText.get_rect().width*0.5, displayHeight*0.4, usernameText.get_rect().width + 50, usernameText.get_rect().height*1.5)

            if resultOption == 1:
                passwordBox = pygame.Rect(displayWidth*0.5 - passwordText.get_rect().width*0.5, displayHeight*0.6, passwordText.get_rect().width+50, passwordText.get_rect().height*1.5)
                sudoBox = pygame.Rect(displayWidth*0.5 - sudoText.get_rect().width*0.5, displayHeight*0.8, sudoText.get_rect().width+50, sudoText.get_rect().height+10*1.5)
                if passwordBox.collidepoint(mousePos):
                    pygame.draw.rect(display, lightGrey, passwordBox)
                else:
                    pygame.draw.rect(display, grey, passwordBox)
                if sudoBox.collidepoint(mousePos):
                    pygame.draw.rect(display, lightGrey, sudoBox)
                else:
                    pygame.draw.rect(display, grey, sudoBox)
                display.blit(passwordText, CenterText(passwordBox, passwordText))
                display.blit(sudoText, CenterText(sudoBox, sudoText))

            if searchInputBox.collidepoint(mousePos):
                pygame.draw.rect(display, lightGrey, searchInputBox)
            else:
                pygame.draw.rect(display, grey, searchInputBox)
            if usernameBox.collidepoint(mousePos):
                pygame.draw.rect(display, lightGrey, usernameBox)
            else:
                pygame.draw.rect(display, grey, usernameBox)
            if returnMenuBox.collidepoint(mousePos):
                pygame.draw.rect(display, lightGrey, returnMenuBox)
            else:
                pygame.draw.rect(display, grey, returnMenuBox)

            if resultsDeleteShow:
                if resultsDeleteBox.collidepoint(mousePos):
                    pygame.draw.rect(display, red, resultsDeleteBox)
                else:
                    pygame.draw.rect(display, darkRed, resultsDeleteBox)
                display.blit(resultsDeleteText, CenterText(resultsDeleteBox, resultsDeleteText))

            inputText = largeText.render(inputTextString, True, white)
                
            display.blit(inputText, CenterText(searchInputBox, inputText))
            display.blit(usernameText, CenterText(usernameBox, usernameText))
            display.blit(returnMenuText, CenterText(returnMenuBox, returnMenuText))

            pygame.display.update()
            clock.tick(60)
            
        while addServer:
                
            display.fill(black)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if focus == 1:
                        if event.key == pygame.K_TAB:
                            focus = 2
                        else:
                            inputTextStringIp = AddText(event, inputTextStringIp, "ip")
                    elif focus == 2:
                        if event.key == pygame.K_TAB:
                            focus = 3
                        else:
                            inputTextStringUsername = AddText(event, inputTextStringUsername)
                    elif focus == 3:
                        if event.key == pygame.K_TAB:
                            focus = 4
                        else:
                            inputTextStringPassword = AddText(event, inputTextStringPassword)
                    elif focus == 4:
                        if event.key == pygame.K_TAB:
                            focus = 1
                        else:
                            inputTextStringSudo = AddText(event, inputTextStringSudo)
                    if event.key == pygame.K_ESCAPE:
                        addServer = False
                        menu = True
                if event.type == pygame.MOUSEMOTION:
                    mousePos = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = event.pos
                    if addServerIpBox.collidepoint(mousePos):
                        focus = 1
                    if addServerUsernameBox.collidepoint(mousePos):
                        focus = 2
                    if addServerPasswordBox.collidepoint(mousePos):
                        focus = 3
                    if addServerSudoBox.collidepoint(mousePos):
                        focus = 4
                    if addServerConfirmBox.collidepoint(mousePos) and len(inputTextStringIp) > 0 and len(inputTextStringUsername) > 0 and len(inputTextStringPassword) > 0 and len(inputTextStringSudo) > 0:
                        inputTextStringDisp = inputTextStringIp
                        inputIp1 = inputTextStringDisp[:inputTextStringDisp.find(".")]
                        inputTextStringDisp = inputTextStringDisp[inputTextStringDisp.find(".")+1:]
                        inputIp2 = inputTextStringDisp[:inputTextStringDisp.find(".")]
                        inputTextStringDisp = inputTextStringDisp[inputTextStringDisp.find(".")+1:]
                        inputIp3 = inputTextStringDisp[:inputTextStringDisp.find(".")]
                        inputTextStringDisp = inputTextStringDisp[inputTextStringDisp.find(".")+1:]
                        inputIp4 = inputTextStringDisp
                        if inputTextStringIp.count(".") == 3 and int(inputIp1) <= 255 and int(inputIp2) <= 255 and int(inputIp3) <= 255 and int(inputIp4) <= 255 and inputTextStringIp not in usernameDict and inputTextStringIp not in passwordDict and inputTextStringIp not in sudoDict:
                            start = datetime.datetime.now().second
                            cycle = 0
                            addServer = False
                            loading = True
                            addServerLoading = True
                            loadingCircle1 = True
                            loadingCircle2 = False
                            loadingCircle3 = False
                            loadingCircle4 = False
                            loadingCircle5 = False
                            loadingCircle6 = False
                            loadingCircle7 = False
                            loadingCircle8 = False
                    elif addServerConfirmBox.collidepoint(mousePos):
                        addServerError = True
                    if returnMenuBox.collidepoint(mousePos):
                        addServer = False
                        menu = True

            addServerIpText = largeText.render("IP: {}".format(inputTextStringIp), True, white)
            addServerUsernameText = largeText.render("Username: {}".format(inputTextStringUsername), True, white)
            addServerPasswordText = largeText.render("Password: {}".format(inputTextStringPassword), True, white)
            addServerSudoText = largeText.render("Sudo: {}".format(inputTextStringSudo), True, white)

            addServerIpBox = pygame.Rect(displayWidth*0.5 - addServerIpText.get_rect().width*0.5, displayHeight*0.1, addServerIpText.get_rect().width + 50, addServerIpText.get_rect().height*1.5)
            addServerUsernameBox = pygame.Rect(displayWidth*0.5-addServerUsernameText.get_rect().width*0.5, displayHeight*0.3, addServerUsernameText.get_rect().width + 50, addServerUsernameText.get_rect().height*1.5)
            addServerPasswordBox = pygame.Rect(displayWidth*0.5 - addServerPasswordText.get_rect().width*0.5, displayHeight*0.5, addServerPasswordText.get_rect().width + 50, addServerPasswordText.get_rect().height*1.5)
            addServerSudoBox = pygame.Rect(displayWidth*0.5 - addServerSudoText.get_rect().width*0.5, displayHeight*0.7, addServerSudoText.get_rect().width + 50, addServerSudoText.get_rect().height*1.5)
        
            if addServerIpBox.collidepoint(mousePos):
                pygame.draw.rect(display, lightGrey, addServerIpBox)
            else:
                pygame.draw.rect(display, grey, addServerIpBox)
            if addServerUsernameBox.collidepoint(mousePos):
                pygame.draw.rect(display, lightGrey, addServerUsernameBox)
            else:
                pygame.draw.rect(display, grey, addServerUsernameBox)
            if addServerPasswordBox.collidepoint(mousePos):
                pygame.draw.rect(display, lightGrey, addServerPasswordBox)
            else:
                pygame.draw.rect(display, grey, addServerPasswordBox)
            if addServerSudoBox.collidepoint(mousePos):
                pygame.draw.rect(display, lightGrey, addServerSudoBox)
            else:
                pygame.draw.rect(display, grey, addServerSudoBox)
            if addServerConfirmBox.collidepoint(mousePos):
                pygame.draw.rect(display, green, addServerConfirmBox)
            else:
                pygame.draw.rect(display, darkGreen, addServerConfirmBox)
            if returnMenuBox.collidepoint(mousePos):
                pygame.draw.rect(display, lightGrey, returnMenuBox)
            else:
                pygame.draw.rect(display, grey, returnMenuBox)

            if addServerError:
                display.blit(addServerErrorText, (10, displayHeight*0.5 - addServerErrorText.get_rect().height*0.5))

            display.blit(addServerIpText, CenterText(addServerIpBox, addServerIpText))
            display.blit(addServerUsernameText, CenterText(addServerUsernameBox, addServerUsernameText))
            display.blit(addServerPasswordText, CenterText(addServerPasswordBox, addServerPasswordText))
            display.blit(addServerSudoText, CenterText(addServerSudoBox, addServerSudoText))
            display.blit(addServerConfirmText, CenterText(addServerConfirmBox, addServerConfirmText))
            display.blit(returnMenuText, CenterText(returnMenuBox, returnMenuText))

            pygame.display.update()
            clock.tick(60)

        while addEmail:
                
            display.fill(black)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key != pygame.K_TAB:
                        if focus == 1:
                            emailInputTextString = AddText(event, emailInputTextString)
                        if focus == 2:
                            emailPasswordInputTextString = AddText(event, emailPasswordInputTextString)
                    if event.key == pygame.K_ESCAPE:
                        addEmail = False
                        menu = True
                    if focus == 1 and event.key == pygame.K_TAB:
                        focus = 2
                    elif focus == 2 and event.key == pygame.K_TAB:
                        focus = 1
                if event.type == pygame.MOUSEMOTION:
                    mousePos = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = event.pos
                    if addEmailEmailBox.collidepoint(mousePos):
                        focus = 1
                    if addEmailPasswordBox.collidepoint(mousePos):
                        focus = 2
                    if returnMenuBox.collidepoint(mousePos):
                        addEmail = False
                        menu = True
                    if addServerConfirmBox.collidepoint(mousePos):
                        try:
                            emailInputTextString.index("@")
                            emailInputTextString.index(".")
                        except ValueError:
                            addEmailError = True
                            addEmailErrorText = largeText.render("Invalid email", True, red)
                        else:
                            if len(emailPasswordInputTextString) > 0:
                                start = datetime.datetime.now().second
                                cycle = 0
                                addEmail = False
                                loading = True
                                addEmailLoading = True
                                loadingCircle1 = True
                                loadingCircle2 = False
                                loadingCircle3 = False
                                loadingCircle4 = False
                                loadingCircle5 = False
                                loadingCircle6 = False
                                loadingCircle7 = False
                                loadingCircle8 = False
                            else:
                                addEmailError = True
                                addEmailErrorText = largeText.render("Password required", True, red)

            addEmailEmailText = largeText.render("Email: {}".format(emailInputTextString), True, white)
            addEmailPasswordText = largeText.render("Password: {}".format(emailPasswordInputTextString), True, white)

            addEmailEmailBox = pygame.Rect(displayWidth*0.5 - addEmailEmailText.get_rect().width*0.5, displayHeight*0.1, addEmailEmailText.get_rect().width + 50, addEmailEmailText.get_rect().height*1.5)
            addEmailPasswordBox = pygame.Rect(displayWidth*0.5 - addEmailPasswordText.get_rect().width*0.5, displayHeight*0.3, addEmailPasswordText.get_rect().width + 50, addEmailPasswordText.get_rect().height*1.5)

            if addEmailEmailBox.collidepoint(mousePos):
                pygame.draw.rect(display, lightGrey, addEmailEmailBox)
            else:
                pygame.draw.rect(display, grey, addEmailEmailBox)
            if addEmailPasswordBox.collidepoint(mousePos):
                pygame.draw.rect(display, lightGrey, addEmailPasswordBox)
            else:
                pygame.draw.rect(display, grey, addEmailPasswordBox)
            if returnMenuBox.collidepoint(mousePos):
                pygame.draw.rect(display, lightGrey, returnMenuBox)
            else:
                pygame.draw.rect(display, grey, returnMenuBox)
            if addServerConfirmBox.collidepoint(mousePos):
                pygame.draw.rect(display, green, addServerConfirmBox)
            else:
                pygame.draw.rect(display, darkGreen, addServerConfirmBox)

            if addEmailError:
                display.blit(addEmailErrorText, (displayWidth*0.5 - addEmailErrorText.get_rect().width*0.5, displayHeight*0.7))

            display.blit(addEmailEmailText, CenterText(addEmailEmailBox, addEmailEmailText))
            display.blit(addEmailPasswordText, CenterText(addEmailPasswordBox, addEmailPasswordText))
            display.blit(returnMenuText, CenterText(returnMenuBox, returnMenuText))
            display.blit(addServerConfirmText, CenterText(addServerConfirmBox, addServerConfirmText))

            pygame.display.update()
            clock.tick(60)

        while addBank:
                
            display.fill(black)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key != pygame.K_TAB:
                        if focus == 1:
                            addBankNumberInputTextString = AddText(event, addBankNumberInputTextString, "number")
                        if focus == 2:
                            addBankPasswordInputTextString = AddText(event, addBankPasswordInputTextString)
                    if event.key == pygame.K_ESCAPE:
                        addBank = False
                        menu = True
                    if focus == 1 and event.key == pygame.K_TAB:
                        focus = 2
                    elif focus == 2 and event.key == pygame.K_TAB:
                        focus = 1
                if event.type == pygame.MOUSEMOTION:
                    mousePos = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = event.pos
                    if addBankNumberBox.collidepoint(mousePos):
                        focus = 1
                    if addBankPasswordBox.collidepoint(mousePos):
                        focus = 2
                    if returnMenuBox.collidepoint(mousePos):
                        addBank = False
                        menu = True
                    if addServerConfirmBox.collidepoint(mousePos):
                        if len(addBankNumberInputTextString) > 0 and len(addBankPasswordInputTextString) > 0:
                            start = datetime.datetime.now().second
                            cycle = 0
                            addBank = False
                            loading = True
                            addBankLoading = True
                            loadingCircle1 = True
                            loadingCircle2 = False
                            loadingCircle3 = False
                            loadingCircle4 = False
                            loadingCircle5 = False
                            loadingCircle6 = False
                            loadingCircle7 = False
                            loadingCircle8 = False
                        else:
                            addBankError = True

            addBankNumberText = largeText.render("Account Number: {}".format(addBankNumberInputTextString), True, white)
            addBankPasswordText = largeText.render("Password: {}".format(addBankPasswordInputTextString), True, white)

            addBankNumberBox = pygame.Rect(displayWidth*0.5 - addBankNumberText.get_rect().width*0.5, displayHeight*0.1, addBankNumberText.get_rect().width + 50, addBankNumberText.get_rect().height*1.5)
            addBankPasswordBox = pygame.Rect(displayWidth*0.5 - addBankPasswordText.get_rect().width*0.5, displayHeight*0.3, addBankPasswordText.get_rect().width + 50, addBankPasswordText.get_rect().height*1.5)

            if addBankNumberBox.collidepoint(mousePos):
                pygame.draw.rect(display, lightGrey, addBankNumberBox)
            else:
                pygame.draw.rect(display, grey, addBankNumberBox)
            if addBankPasswordBox.collidepoint(mousePos):
                pygame.draw.rect(display, lightGrey, addBankPasswordBox)
            else:
                pygame.draw.rect(display, grey, addBankPasswordBox)
            if returnMenuBox.collidepoint(mousePos):
                pygame.draw.rect(display, lightGrey, returnMenuBox)
            else:
                pygame.draw.rect(display, grey, returnMenuBox)
            if addServerConfirmBox.collidepoint(mousePos):
                pygame.draw.rect(display, green, addServerConfirmBox)
            else:
                pygame.draw.rect(display, darkGreen, addServerConfirmBox)

            if addBankError:
                display.blit(addBankErrorText, (displayWidth*0.5 - addBankErrorText.get_rect().width*0.5, displayHeight*0.7))

            display.blit(addBankNumberText, CenterText(addBankNumberBox, addBankNumberText))
            display.blit(addBankPasswordText, CenterText(addBankPasswordBox, addBankPasswordText))
            display.blit(returnMenuText, CenterText(returnMenuBox, returnMenuText))
            display.blit(addServerConfirmText, CenterText(addServerConfirmBox, addServerConfirmText))

            pygame.display.update()
            clock.tick(60)

        while viewDatabase:
                
            display.fill(black)

            if not smallerText:
                i = 10
            else:
                i = 5

            pygame.draw.rect(display, darkRed, databaseHeaderBox)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEMOTION:
                    mousePos = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = event.pos
                    if returnMenuBox.collidepoint(mousePos):
                        viewDatabase = False
                        menu = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        viewDatabase = False
                        menu = True

            databaseIpBox.height = len(databaseIpList) * 30 + 20

            if databaseIpBox.height >= displayHeight - (databaseHeaderBox.y + databaseHeaderBox.height):
                databaseIpBox.height = displayHeight - (databaseHeaderBox.y + databaseHeaderBox.height) - 20

            pygame.draw.rect(display, red, databaseIpBox)

            if returnMenuBox.collidepoint(mousePos):
                pygame.draw.rect(display, lightGrey, returnMenuBox)
            else:
                pygame.draw.rect(display, grey, returnMenuBox)

            display.blit(returnMenuText, CenterText(returnMenuBox, returnMenuText))
            display.blit(databaseHeaderText, CenterText(databaseHeaderBox, databaseHeaderText))
            for ip in databaseIpList:
                databaseIpText = smallText.render(ip, True, white)
                display.blit(databaseIpText, (databaseIpBox.x + databaseIpBox.width*0.5 - databaseIpText.get_rect().width*0.5, databaseIpBox.y + i))
                if not smallerText:
                    i += 30
                else:
                    i += 15

            pygame.display.update()
            clock.tick(60)

if __name__=="__main__":
    IpDatabase()
