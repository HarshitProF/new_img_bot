## Author: Omar Medhat Aly
## Company: Upwork
## Project: Milstone 2
## Last Date of Modification: 19.04.2023

## importing the desired Packages
#import cv2 as cv
import sys
from PIL import Image, ImageFont, ImageDraw
from PIL.ImageEnhance import Sharpness,Brightness,Color,Contrast

class MODIFICATION:
    """
    The Main Class for the Disered Target of this Project
    """
    def __init__(self, img,cross:str=None,Situation:str=None,percentage:str=None,last_price:str=None,referral_code:str=None ,Risk:str=None,Entry_Price:str=None,Mark_Price:str=None,Liq_Price:str=None, Perpetual:str=None,Unrealized_PNL:str=None,ROE:str=None,Size:str=None,Margin:str=None,type="type_a",font_size_Perpetual=44) :

        self.img = img ## assign the Image directory 
        
        try:
            self.img = Image.open(self.img) ## reading the Image to be modified
        except FileNotFoundError as e:
            print(f"The Assigend Image Directory isn't Corret, so that you got {e} Error\n\nRe-read that Again {MODIFICATION.__init__.__doc__}")
            sys.exit(1)
        
        self.type = type
        self.font_per = font_size_Perpetual

        if self.type == 'type_a': 
            ## adding your Modified Inputs
            self.cross = str(cross)
            self.Perpetual = str(Perpetual) #input("Enter Perpetual : ") ## Try not to exceed 9 Characters not to be spoiled out
            self.Unrealized_PNL =str(Unrealized_PNL) #input("Enter Unrealized PNL (USDT) : ")
            self.ROE =str(ROE) #input("Enter ROE % : ")
            self.Size =str(Size) #input("Enter Size (USDT) : ")
            self.Margin =str(Margin) #input("Enter Margin (USDT) : ")
            self.Risk =str(Risk) #input("Enter Risk % : ")
            self.Entry_Price =str(Entry_Price) #input("Enter Entry Price : ")
            self.Mark_Price =str(Mark_Price) #input("Enter Mark Price : ")
            self.Liq_Price =str(Liq_Price) #input("Enter Liq.Price : ")
            # self.TP = str(input("Enter TP : "))
            # self.SL = str(input("Enter SL : "))
            
            
        else:
            self.Cross =str(cross) #input("Enter Cross Value [Default: 20x]: ")
            self.Perpetual =str(Perpetual) #input("Enter Perpetual : ") ## Try not to exceed 9 Characters not to be spoiled out
            self.Situation =str(Situation) #str(input("Enter Situation [LONG / SHORT]: "))
            self.percentage =str(percentage) #input("Enter the Percentage: ")
            self.entry_price =str(Entry_Price) #input("Enter Entry Price: ")
            self.last_price =str(last_price) #input("Enter Last Price: ")
            self.referral_code =str(referral_code) #input("Enter Referral Code: ")

    def WriteOnImage_type_a(self,mark1:str="raw",mark2:str="raw",mark3:str="raw",mark4:str="raw", TP_SL:bool= False, change_exclamation_mark:bool = True, show_image:bool=True, save_image:bool=True):
        """
        TP_SL: for Type A Images without TP/SL you can set it to False when you call it down
            e.g. MODIFICATION(..).WriteOnImage_type_a(..., TP_SL=False, ...)

        change_exclamation_mark: To Change the Color of The Exclamation Mark, Always choose to change the Four Marks in order to have the Full Freedom
        """
        raw_exclamation_mark = Image.open("raw_exclamation_mark.jpg")
        red_exclamation_mark = Image.open("red_exclamation_mark.jpg")
        green_exclamation_mark = Image.open("green_exclamation_mark.jpg")
        if len(self.Perpetual)>=8:
            s=len(self.Perpetual)-8
            p=35+30*s
        else:
            p=0
        print(p)
        ## The Title
        font = ImageFont.truetype("fonts/IBMPlexArabic-Medium.ttf", self.font_per)
        draw = ImageDraw.Draw(self.img)
        draw.text((110,30), self.Perpetual, (255,255,255), font=font)

        """## Cross
        #550
        font_ = ImageFont.truetype("IBMPlexArabic-Medium.ttf", 35)
        draw.text((550+p,40), self.cross, (136,142,154), font=font_)"""
        #Perpentual
        if p==0:
            t=0
        else:
            t=p-30
        per_mask_position=(324+t,39)
        Perpetual_mask=Image.open('perpentual.jpg')
        self.img.paste(Perpetual_mask,per_mask_position)

        ## Unrealized PNL & ROE
        font_2 = ImageFont.truetype("fonts/DIN_Medium.ttf", 56) ## after many experiments we got that 56 is an ideal Font size 
        draw = ImageDraw.Draw(self.img)
        draw.text((46,200), self.Unrealized_PNL, (45,188,132), font=font_2) ## green color with specific location ==> Unrealized PNL
        font_3 = ImageFont.truetype("fonts/DIN_Bold.ttf", 56)
        draw = ImageDraw.Draw(self.img)
        #788
        print(len(self.ROE))
        if len(self.ROE)<=5:
            q=6-len(self.ROE)
            r=30*q
        else:
            r=0
        print(r)
        draw.text((788+r,200), f"+ {self.ROE}%", (45,188,132), font=font_2) ## green color with specific location ==> ROE
       

        ## Size & Margin
        font_4 = ImageFont.truetype("fonts/DIN_Medium.ttf", 40)
        draw = ImageDraw.Draw(self.img)
        draw.text((43,340), self.Size, (255,255,255), font=font_4)
        draw.text((403,340), self.Margin, (255,255,255), font=font_4)

        ## Risk
        if len(self.Risk)>=4:
            rp=(len(self.Risk)-3)*4
        else:
            rp=(len(self.Risk)-3)*4
        font_5 = ImageFont.truetype("fonts/DIN_Medium.ttf", 39)
        draw = ImageDraw.Draw(self.img)
        draw.text((930-rp,340), f"{self.Risk}%", (45,188,132), font=font_5) 

        ## Entry Price & Mark Price
        font_6 = ImageFont.truetype("fonts/DIN_Medium.ttf", 40)
        draw = ImageDraw.Draw(self.img)
        draw.text((43,466), self.Entry_Price, (255,255,255), font=font_6)
        draw.text((403,466), self.Mark_Price, (255,255,255), font=font_6)

        ## Liq Price
        if len(self.Liq_Price)>5:
            qt=(len(self.Liq_Price)-5)*15
        else:
            qt=0
        print(qt)
        font_7 = ImageFont.truetype("fonts/DIN_Bold.ttf", 33)
        draw = ImageDraw.Draw(self.img)
        draw.text((939-qt,466), self.Liq_Price, (255,255,255), font=font_7)
        
        ## TP & SL
        if TP_SL:

            self.TP = str(input("Enter TP : "))
            self.SL = str(input("Enter SL : "))

            font_8 = ImageFont.truetype("fonts/DIN_Medium.ttf", 39)
            draw = ImageDraw.Draw(self.img)
            draw.text((170,550), f"{self.TP} / {self.SL}", (255,255,255), font=font_8)

        if change_exclamation_mark:
            """try:
                number_of_marks =marks #int(input("Enter Number of Exclamation Marks you're willing to change [4 MAX.] : "))
            except ValueError:
                print("Enter an Integer Number")
            except UnboundLocalError:
                print("You've forgotten to enter the Value :)")"""

            mask_position = (725,36)
            Position_1 = (728+20+t,36)
            Position_2 = (744+t+20,36)
            Position_3 = (758+t+20,36)
            Position_4 = (775+t+20,36)

            mask = Image.open('mask.jpg')
            self.img.paste(mask, mask_position)
            if mark1=="raw":
                ex=raw_exclamation_mark
                self.img.paste(ex,Position_1)
            elif mark1=="red":
                ex=red_exclamation_mark
                self.img.paste(ex,Position_1)
            else :
                ex=green_exclamation_mark
                self.img.paste(ex,Position_1)
            if mark2=="raw":
                ex=raw_exclamation_mark
                self.img.paste(ex,Position_2)
            elif mark2=="red":
                ex=red_exclamation_mark
                self.img.paste(ex,Position_2)
            else :
                ex=green_exclamation_mark
                self.img.paste(ex,Position_2)
            if mark3=="raw":
                ex=raw_exclamation_mark
                self.img.paste(ex,Position_3)
            elif mark3=="red":
                ex=red_exclamation_mark
                self.img.paste(ex,Position_3)
            else :
                ex=green_exclamation_mark
                self.img.paste(ex,Position_3)
            if mark4=="raw":
                ex=raw_exclamation_mark
                self.img.paste(ex,Position_4)
            elif mark4=="red":
                ex=red_exclamation_mark
                self.img.paste(ex,Position_4)
            else :
                ex=green_exclamation_mark
                self.img.paste(ex,Position_4)
        ## Cross
        #550
        font_ = ImageFont.truetype("fonts/IBMPlexArabic-Medium.ttf", 35)
        draw.text((560+t,40), self.cross, (136,142,154), font=font_)

        #Enhance Sharpness
        self.img=Sharpness(self.img).enhance(factor=1)
        #Brightness
        self.img=Brightness(self.img).enhance(factor=1)
        #enhance color
        self.img=Color(self.img).enhance(factor=1)
        #Enhance Contrast
        self.img=Contrast(self.img).enhance(factor=1.2)
            
            

        #if show_image: self.__show_image()

        if save_image: self.__save_image()
        return self.img

    def WriteOnImage_type_b(self, show_image:bool=False, save_image:bool=True):
        ## Perpetual
        font = ImageFont.truetype("fonts/DIN_Medium.ttf", 21)
        draw = ImageDraw.Draw(self.img)
        draw.text((278,128), self.Perpetual, (255,255,255), font=font)

        ## cross Value
        font = ImageFont.truetype("fonts/DIN_Medium.ttf", 22)
        draw = ImageDraw.Draw(self.img)
        draw.text((212,127), self.Cross, (255,255,255), font=font)
        perpentual_2=Image.open('saved/perpentual_2.jpg')
        if len(self.Perpetual)>7:
            r=len(self.Perpetual)-7
        else:
            r=0
        Position_perpentual=(372+12*r,121)
        self.img.paste(perpentual_2,Position_perpentual)

        ## Situation
        if self.Situation == "LONG":
            font = ImageFont.truetype("fonts/IBMPlexArabic-Medium.ttf", 22)
            draw = ImageDraw.Draw(self.img)
            draw.text((102,120), self.Situation, (45,188,132), font=font)
        elif self.Situation == "SHORT":
            font = ImageFont.truetype("fonts/IBMPlexArabic-Medium.ttf", 22)
            draw = ImageDraw.Draw(self.img)
            draw.text((102,120), self.Situation, (178,45,78), font=font)
        else:
            font = ImageFont.truetype("fonts/IBMPlexArabic-Medium.ttf", 22)
            draw = ImageDraw.Draw(self.img)
            draw.text((102,120), self.Situation, (45,188,132), font=font)

        ## Percentage
        #84 
        font1 = ImageFont.truetype("fonts/DIN_Bold.ttf", 84)
        draw = ImageDraw.Draw(self.img)
        draw.text((98,152), f"+ {self.percentage}%", (45,188,132), font=font1)

        font = ImageFont.truetype("fonts/DIN_Medium.ttf", 34)
        draw = ImageDraw.Draw(self.img)
        ## Last Price
        draw.text((298,356), self.last_price, (235,180,35), font=font)
        ## Entry Price
        draw.text((298,294), self.entry_price, (235,180,35), font=font)

        ## referral Code
        font = ImageFont.truetype("fonts/DIN_Medium.ttf", 42)
        draw = ImageDraw.Draw(self.img)
        draw.text((198,442), self.referral_code, (255, 255, 255), font=font)


        #Enhance Sharpness
        self.img=Sharpness(self.img).enhance(factor=1)
        #Brightness
        self.img=Brightness(self.img).enhance(factor=1)
        #enhance color
        self.img=Color(self.img).enhance(factor=1)
        #Enhance Contrast
        self.img=Contrast(self.img).enhance(factor=1.2)


        if show_image: self.__show_image()

        if save_image: self.__save_image()
        return self.img

    def __save_image(self, name="Exclamation_mark_Changed"):
        self.img.save(f"{name}.png")

    def __show_image(self):
        self.img.show()

## Example to run the script on
### YOU SHOULD NOTICE THAT BY APPLING "type_b" YOU SHOULD CALL THE METHOD RELATED TO THAT TYPE [WriteOnImage_type_b] , same for the Other Type
#MODIFICATION("saved/Type_A_5[no TP-SL][no25x].jpg", "type_a").WriteOnImage_type_a(show_image=True, TP_SL=False, save_image=False, change_exclamation_mark=True)
# MODIFICATION("saved/Type_D.JPG", "type_b").WriteOnImage_type_b(show_image=True, save_image=False)


""" 

        ============================>>>>> INSTRUCTIONS <<<<<============================

## The Following Photos must be called with [ MODIFICATION(PATH, "type_a").WriteOnImage_type_a(....) ] :
[1] saved/Type_A_1.jpg
[2] saved/Type_A_2.jpg
[3] saved/Type_A_3.jpg [NOTE: 20x is already here exists]
[4] saved/Type_A_4[no TP-SL][no25x].jpg
[5] saved/Type_A_5[no TP-SL][no25x].jpg

## The Following Photos must be called with [ MODIFICATION(PATH, "type_b").WriteOnImage_type_b(....) ] :
[1] saved/Type_B.jpg
[2] saved/Type_C.JPG
[3] saved/Type_D.JPG


"""