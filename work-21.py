#8-misol
 #   D = int(input("Kun: "))
 #  M = int(input("Oy: "))

  #  match M:
   #     case 1: oy_nomi = "Yanvar"; max_kun = 31
    #    case 2: oy_nomi = "Fevral"; max_kun = 28
     #   case 3: oy_nomi = "Mart"; max_kun = 31
      #  case 4: oy_nomi = "Aprel"; max_kun = 30
       # case 5: oy_nomi = "May"; max_kun = 31
        #case 6: oy_nomi = "Iyun"; max_kun = 30
  #      case 7: oy_nomi = "Iyul"; max_kun = 31
   #     case 8: oy_nomi = "Avgust"; max_kun = 31
    #    case 9: oy_nomi = "Sentabr"; max_kun = 30
     #   case 10: oy_nomi = "Oktabr"; max_kun = 31
      #  case 11: oy_nomi = "Noyabr"; max_kun = 30
       # case 12: oy_nomi = "Dekabr"; max_kun = 31
     #   case _:
      #      print("Xato oy!")
       #     return

    #if 1 <= D <= max_kun:
    #    print(f"{D}-{oy_nomi}")
    #else:
     #   print("Xato sana!")

#while True:
 #   print("\n--- MENU ---")
  #  print("1 - Case1")
   # print("2 - Case2")
    #print("3 - Case3")
   # print("4 - Case4")
   # print("5 - Case5")
   # print("6 - Case6")
   # print("7 - Case7")
   # print("8 - Case8")
   # print("0 - Chiqish")

   # tanlov = int(input("Tanlang: "))

    #match tanlov:
     #   case 1: case1()
      #  case 2: case2()
       # case 3: case3()
        #case 4: case4()
#        case 5: case5()
 #       case 6: case6()
  #      case 7: case7()
   #     case 8: case8()
    #    case 0: break
     #   case _: print("Noto'g'ri tanlov!")
#9-misol
#d=int(input("d="))
#m=int(input("m="))
#match m:
#case 1 | 3 | 5 | 7 | 8 | 10 :
#    if d<31:
#        d+=1
#    else:
#        d=1
#        m+=1
##    case 4 | 6 | 9 | 11:
 #           if d<30:
 #           d+=1
#    else:
#            d=1
#            m+=1
#    case 2:
#        if d<28:
#            d+=1 
#    else:
#        d=1
#        m+=13    case 12:
#    if d<31:
#        d+=1 
#    else:
#        d=1
#        m=1
#    print("Keyingi sana")

#10-misol
#Y=int(input("Y="))
#K=int(input("K="))
#match K :
#    case 0:
#        print("davom ettiradi")
#    case 1:
#        print("chapga buriladi")
 #   case 2:
 #       print("o'ngga buriladi")
#match Y:
#    case 1:
#        print("Shimol")
#    case 2:
 #       print("janub")
#    case 3:
#        print("sharq")
#    case 4:
#        print("g'arb")
#11-misol
#k1=int(input("k1="))
#k2=int(input("k2="))
#match k1:
#    case 1:
#        print("shimolni ko'rsatadi")
#    case 2:
#        print("janubni ko'rsatadi")
#    case 3:
#        print("sharqni ko'rsatadi")
#    case 4:
#        print("G'arbni ko'rsatadi")
#match k2:
#    case 0:
#        print("O'nga buriladi")
#    case 1:
#        prit("chapga buriladi")
#    case 2:
#        print("Orqaga buriladi")

#12-misol      

#A=int(input("Berilgan son="))
#B=int(input("Doira elementi nomi="))
#pi=3.14
#match B:
#    case 1:
#      print("Diametri=",2*A,"Uzunligi=",2*pi*A,"Yuzasi=",pi*pow(A,2))
#    case 2:
#      print("Radiusi",A/2,"Uzunligi=",pi*A,"Yuzasi",pi*pow(A/2,2))
#    case 3:
#       print("Radiusi=",A/(pi*2),"Diametri=",A/(pi),"Yuzasi=",pow((A/(pi*2)),2)*pi)
#    case 4:
#        print(pow("Radiusi=",pow(A/pi,1/2),"Diametri=",pow(A/pi,1/2)*2,"Uzunligi=",pow(A/pi,1/2)*pi*2))
#13
#a=int(input("berilgan son="))
#b=int(input('doira element nomi='))
#match b:
#    case 1:
#        print("gipatenuza=", a*pow(2, 1/2),"balandlik=", a*pow(2, 1/2)/2, "yuzasi=", (a*pow(2, 1/2))**2/4)
#    case 2:
#        print("kateti=", a/pow(2, 1/2), "balandlik=", a/2, "yuzasi=", a**2/4)
#    case 3:
#        print("gipatenuza=", a*pow(2,1/2),"balandligi",pow(a,2))
#    case 4:
#        print()
#'''ustoz davomini ishlamadim'''
#14 misol
#a=int(input("berilgan son="))
#k=int(input("uchburchakning bir qiymatini tanlang="))
#match k:
#    case 1:
#        print("R1=", a*pow(3, 1/2)/6, "R2=", a*pow(3, 1/2)/3, "Yuzasi=", a**2*pow(3, 1/2)/4)
#    case 2:
#        print("a=", 6*a/pow(3, 1/2), "R2=", 2*a, "yuzasi=", pow(6*a/pow(3, 1/2), 2)*pow(3, 1/2)/4)
#    case 3:
#        print("R1=", a/2, "a=", a*3/pow(3, 1/3), "yuzasi=", pow(a*3/pow(3, 1/3), 2)*pow(3, 1/2)/4)
#    case 4:
#        print("a=", pow(a*4/pow(3, 1/2), 1/2), "R1=", pow(a*4/pow(3, 1/2), 1/2)*pow(3, 1/2)/4, "R2=", pow(a*4/(pow(3, 1/2)), (1/2))*pow(3, 1/2)/2)

#case15
#M=int(input("karta turi"))
#N=int(input("Karta qiymati"))
#match M:
#    case 1:
#        print("g'isht")
#    case 2:
#        print("olma")
#    case 3:
#        print("chillak")
#    case 4:
#        print("qarg'a")
#    case _:
#        print("kartaning bunday turi yo'q")
#match N:
#        case 6:
#            print(6)
#        case 7:
#            print(7)
#        case 8:
#            print(8)
#       case 9:
#           print(9)
#        case 10:
#            print(10)
#       case 11:
#            print("valet")
#        case 12:
#            print("dama")
#        case 13:
#            print("qirol")
#        case 14:
#            print("tuz")
#        case _:
#            print("bunday qiymat yoq")
#16-misol
#son=int(input("yoshingni kirit ( 20-69):"))
#birlik=son%10
#onlik=son//10*10
#match onlik:
#    case 20:
#        print("yigirma")
#   case 30:
#       print("o'ttiz")
#   case 40:
#       print("qirq")
#    case 50:
#        print("alli")
#    case 60:
#        print("oltmish")
#match birlik:
#    case 1:
#        print("bir")
#   case 2:
#       print("ikki")
#   case 3:
#       print("uch")
#    case 4:
#       print("to'rt")
#   case 5:
#       print("besh")
#    case 6:
#        print("olti")
#    case 7:
#       print("yetti")
#    case 8:
#       print("sakkiz")
#       print(onlik+birlik)

