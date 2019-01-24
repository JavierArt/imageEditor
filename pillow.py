from PIL import ImageFilter, ImageOps, ImageDraw,ImageFont,ImageEnhance
from tkinter import *
from PIL import Image
from os import listdir
import time

class ScrolledFrame(Frame):
    def __init__(self, master=None, *args, **kwargs):
        top = Frame(master)  # create top frame, containing all things
        # attach scrollbars
        vscroll = Scrollbar(top)
        vscroll.pack(side='right', fill='y')
        hscroll = Scrollbar(top, orient='horizontal')
        hscroll.pack(side='bottom', fill='x')
        # hack: insert self into scrollable canvas
        canvas = Canvas(top, highlightthickness=0)
        canvas.pack(expand=True, fill='both')
        super().__init__(master=canvas, *args, **kwargs)  # create
        canvas.create_window(0,0, window=self,
                             anchor='nw', tags='frame')  # insert
        # add a hack to rebuild scrollable area size
        canvas.bind('<Configure>', self.__set_scroll)
        # cross-bind scrolling
        vscroll['command'] = canvas.yview
        canvas['yscrollcommand'] = vscroll.set
        hscroll['command'] = canvas.xview
        canvas['xscrollcommand'] = hscroll.set
        # attach hierarchically
        self._top = top
        self._top._vscroll = vscroll
        self._top._hscroll = hscroll
        self._top._canvas = canvas

    def pack(self, *args, **kwargs):
        '''
        A wrapper over tkinter's pack
        '''
        return self._top.pack(*args, **kwargs) # pack topmost

    def __set_scroll(self, event=None):
        canvas = self._top._canvas
        canvas.config(scrollregion=canvas.bbox('frame'))

def showcolors(colors):
    colors = colors[:]
    root = Tk()
    root.title('Tkinter colors showcase')
    Label(root, text='Double click select color').pack(fill='x')
    top = ScrolledFrame(root)
    colnum = int((len(colors)/3) ** 0.5)
    row = 0
    while colors:
        chunk, colors = colors[:colnum], colors[colnum:]
        for col, color in enumerate(chunk):
            lab = Label(top, text=color, bg=color)
            lab.grid(row=row, column=col, sticky='wens')
            lab.bind('<Double-1>', _clipboard_copy(lab))
            lab.bind('<Enter>', lambda ev, lab=lab: lab.config(fg='white'))
            lab.bind('<Leave>', lambda ev, lab=lab: lab.config(fg='black'))
        row += 1
    top.pack(expand=True, fill='both')
    root.mainloop()

def showcolorsT2(colors):
    colors = colors[:]
    root = Tk()
    root.title('Tkinter colors showcase')
    Label(root, text='Double click to select color').pack(fill='x')
    top = ScrolledFrame(root)
    colnum = int((len(colors)/3) ** 0.5)
    row = 0
    while colors:
        chunk, colors = colors[:colnum], colors[colnum:]
        for col, color in enumerate(chunk):
            lab = Label(top, text=color, bg=color)
            lab.grid(row=row, column=col, sticky='wens')
            lab.bind('<Double-1>', _clipboard_copyT2(lab))
            lab.bind('<Enter>', lambda ev, lab=lab: lab.config(fg='white'))
            lab.bind('<Leave>', lambda ev, lab=lab: lab.config(fg='black'))
        row += 1
    top.pack(expand=True, fill='both')
    root.mainloop()

def showcolorsC3(colors):
    colors = colors[:]
    root = Tk()
    root.title('Tkinter colors showcase')
    Label(root, text='Double click to select color').pack(fill='x')
    top = ScrolledFrame(root)
    colnum = int((len(colors)/3) ** 0.5)
    row = 0
    while colors:
        chunk, colors = colors[:colnum], colors[colnum:]
        for col, color in enumerate(chunk):
            lab = Label(top, text=color, bg=color)
            lab.grid(row=row, column=col, sticky='wens')
            lab.bind('<Double-1>', _clipboard_copyC3(lab))
            lab.bind('<Enter>', lambda ev, lab=lab: lab.config(fg='white'))
            lab.bind('<Leave>', lambda ev, lab=lab: lab.config(fg='black'))
        row += 1
    top.pack(expand=True, fill='both')
    root.mainloop()

COLORS = ['snow', 'ghostwhite', 'whitesmoke', 'gainsboro', 'floralwhite', 'old lace',
          'linen', 'antiquewhite', 'papayawhip', 'blanchedalmond', 'bisque', 'peachpuff',
          'navajowhite', 'lemonchiffon', 'mintcream', 'azure', 'aliceblue', 'lavender',
          'lavenderblush', 'mistyrose', 'darkslategray', 'dimgray', 'slategray',
          'lightslategray', 'gray', 'lightgrey', 'midnightblue', 'navy', 'cornflowerblue', 'darkslateblue',
          'slateblue', 'mediumslateblue', 'lightslateblue', 'mediumblue', 'royalblue',  'blue',
          'dodgerblue', 'deepskyblue', 'skyblue', 'lightskyblue', 'steelblue', 'lightsteelblue',
          'lightblue', 'powderblue', 'paleturquoise', 'darkturquoise', 'mediumturquoise', 'turquoise',
          'cyan', 'lightcyan', 'cadetblue', 'mediumaquamarine', 'aquamarine', 'darkgreen', 'darkolivegreen',
          'darkseagreen', 'seagreen', 'mediumseagreen', 'lightseagreen', 'palegreen', 'springgreen',
          'lawngreen', 'mediumspringgreen', 'greenyellow', 'limegreen', 'yellowgreen',
          'forestgreen', 'olivedrab', 'darkkhaki', 'khaki', 'palegoldenrod', 'lightgoldenrodyellow',
          'lightyellow', 'yellow', 'gold', 'lightgoldenrod', 'goldenrod', 'darkgoldenrod', 'rosybrown',
          'indianred', 'saddlebrown', 'sandybrown',
          'darksalmon', 'salmon', 'light salmon', 'orange', 'dark orange',
          'coral', 'lightcoral', 'tomato', 'orangered', 'red', 'hotpink', 'deeppink', 'pink', 'lightpink',
          'palevioletred', 'maroon', 'mediumvioletred', 'violetred',
          'mediumorchid', 'darkorchid', 'darkviolet', 'blueviolet', 'purple', 'mediumpurple',
          'thistle','black','wheat']

pic=input("Arrastre el archivo escriba la ruta, el nombre y extension de la imagen a modificar:")
picture=pic.replace("\"","")
try:
    img = Image.open(picture)
except:
    print("No se encontro la imagen, el programa se cerrara")
    time.sleep(3)
    exit(0)

def saveimg(confirm, gen_img):
	if confirm=="s" or confirm=="S":
		name=input("Dime el nombre con extension:")
		gen_img.save(name)
	elif confirm=="n" or confirm=="N":
		print("Imagen no guardada")

def information(img):
    """prints information from the opened image"""
    try:
        print("Tamaño:{}".format(img.size))
        print("Formato:{}".format(img.format))
        print("Modo:{}".format(img.mode))
        img.show()
    except:
        print("No se pudo realizar la operacion")

def cropp(img):
    """takes a part of the image based on the coordenades of area"""
    print("De que forma deseas cortar la imagen")
    print("1.cuadrado\n2.definir area")
    h=input("Seleccione una opcion:")
    try:
	    print("Tamaño de la imagen escogida")
	    print(img.size)
	    if h == "1":
	        val=input("Seleccione el valor a cortar:")
	        cropped_img = ImageOps.crop(img, border=int(val))
	    elif h == "2":
	        prim=input("Seleccione el primer valor 1 arriba izquierda (hacia derecha):")
	        seg=input("Seleccione el segundo valor 2 arriba izquierda (hacia abajo):")
	        ter=input("Seleccione el tercer valor 3 abajo derecha (hacia derecha):")
	        cuar=input("Seleccione el cuarto valor 4 abajo derecha (hacia abajo):")
	        area = (int(prim),int(seg),int(ter),int(cuar))
	        cropped_img = img.crop(area)
	    print(cropped_img.size)
	    cropped_img.show()
	    yn = input("Quieres guardar(s/n):")
	    saveimg(yn, cropped_img)
    except:
        print("El area elegida excede el tamaño de la imagen")

def channels(img):
    """shows RGB and mode from the opened image"""
    try:
        print(img.mode)
        r, g, b = img.split()
        r.show()
        ynr=input("Quieres guardar(red)(s/n):")
        saveimg(ynr,r)
        g.show()
        yng=input("Quieres guardar(green)(s/n):")
        saveimg(yng, g)
        b.show()
        ynb=input("Quieres guardar(blue)(s/n):")
        saveimg(ynb, b)
    except:
        print("No se pudo realizar la operacion")

def merge(img):
    """takes channels and combines them back"""
    try:
        r,g,b = img.split()
        print("1.rbg\n2.brg\n3.bgr\n4.grb\n5.gbr\n")
        opc=input("Seleccione una opcion:")
        if opc=="1":
            new_img = Image.merge("RGB",(r,b,g))
        elif opc=="2":
            new_img = Image.merge("RGB",(b,r,g))
        elif opc=="3":
            new_img = Image.merge("RGB",(b,g,r))
        elif opc=="4":
            new_img = Image.merge("RGB",(g,r,b))
        elif opc=="5":
            new_img = Image.merge("RGB",(g,b,r))
        else:
            print("Esa no vale")
        new_img.show()
        yn=input("Quieres guardar(s/n):")
        saveimg(yn,new_img)
    except:
        print("No se pudo realizar la operacion")

def merge2():
    """takes channels from images and combines them back"""
    print("Las imagenes se cambiaran de tamaño para que se puedan mezclar")
    try:
        print("1.dos imagenes\n2.tres imagenes")
        op=input("Cuantas imagenes desea utilizar:")
        if op == "1":
            pic=input("Escriba la ruta, el nombre y formato de la imagen a modificar:")
            picture1=pic.replace("\"","")
            pic2=input("Escriba la ruta, el nombre y formato de la segunda imagen a unir:")
            picture2=pic2.replace("\"","")
            img = Image.open(picture1)
            an,lar=img.size
            img2 = Image.open(picture2)
            resized = img2.resize((an,lar),Image.ANTIALIAS)
            r1,g1,b1 = img.split()
            r2,g2,b2 = resized.split()
            diccionario={"1":r1,"2":g1,"3":b1,"4":r2,"5":g2,"6":b2}
            print("1:rojo1\n2:verde1\n3.azul1\n4:rojo2\n5:verde2\n6:azul2\n")
            first=input("Seleccione el parametro:")
            second=input("Seleccione el parametro:")
            third=input("Seleccione el parametro:")
            new_pic = Image.merge("RGB",(diccionario[first],diccionario[second],diccionario[third]))
            new_pic.show()
            yn=input("Quieres guardar(s/n):")
            if yn=="s":
                quality_val=90
                name=input("Dime el nombre con extension:")
                new_pic.save(name,quality=quality_val)
            elif yn=="n":
                print("Imagen no guardada")
        elif op == "2":
            pic21=input("Escriba la ruta, el nombre y formato de la imagen a modificar:")
            picture1=pic21.replace("\"","")
            pic22=input("Escriba la ruta, el nombre y formato de la imagen a modificar:")
            picture2=pic22.replace("\"","")
            pic23=input("Escriba la ruta, el nombre y formato de la imagen a modificar:")
            picture3=pic23.replace("\"","")
            img = Image.open(picture1)
            ancho,largo=img.size
            img2 = Image.open(picture2)
            resized = img.resize((ancho,largo))
            img3 = Image.open(picture3)
            resized2 = img.resize((ancho,largo))
            r1,g1,b1 = img.split()
            r2,g2,b2 = resized.split()
            r3,g3,b3 = resized2.split()
            diccionario={"1":r1,"2":g1,"3":b1,"4":r2,"5":g2,"6":b2,"7":r3,"8":g3,"9":b3}
            print("1:rojo1\n2:verde1\n3.azul1\n4:rojo2\n5:verde2\n6:azul2\n7:rojo3\n8:verde3\n9:azul3\n")
            first=input("Seleccione el parametro:")
            second=input("Seleccione el parametro:")
            third=input("Seleccione el parametro:")
            new_pic = Image.merge("RGB",(diccionario[first],diccionario[second],diccionario[third]))
            new_pic.show()
            yn = input("Quieres guardar(s/n):")
            if yn=="y":
            	quality_val=90
            	name=input("Dime el nombre con extension:")
            	new_pic.save(name,quality=quality_val)
            elif yn=="n":
                print("Imagen no guardada")
        else:
            print("Esa no vale")
    except:
        print("No se pudo realizar la operacion")

def resize(img):
    """takes a picture and resize it"""
    try:
        first=input("Ingresa coordenada 1:")
        second=input("Ingresa coordenada 2:")
        resized = img.resize((int(first),int(second)),Image.ANTIALIAS)
        resized.show()
        yn=input("Quieres guardar(s/n):")
        saveimg(yn,resized)
    except:
        print("No se pudo realizar la operacion")

def fliplr(img):
    """takes a picture and flips it"""
    try:
        print("1.FLIP_TOP_BOTTOM\n2.FLIP_LEFT_RIGHT")
        y=input("Seleccione una opcion:")
        if y == "1":
            flippic= img.transpose(Image.FLIP_TOP_BOTTOM)
        elif y == "2":
            flippic= img.transpose(Image.FLIP_LEFT_RIGHT)
        else:
            print("Esa no vale")
        flippic.show()
        yn=input("Quieres guardar(s/n):")
        saveimg(yn,flippic)
    except:
        print("No se pudo realizar la operacion")

def rotate(img):
    """takes a picture and rotates it"""
    try:
        print("1.90\n2.180\n3.270\n4.definir num grados")
        z=input("Elija una opcion:")
        if z == "1":
            rotpic= img.transpose(Image.ROTATE_90)
        elif z == "2":
            rotpic= img.transpose(Image.ROTATE_180)
        elif z == "3":
            rotpic= img.transpose(Image.ROTATE_270)
        elif z=="4":
            grad=input("Cuantos grados deseas rotar la imagen:")
            rotpic=img.rotate(int(grad))
        else:
            print("Esa no vale")
        rotpic.show()
        yn=input("Quieres guardar(s/n):")
        if yn=="y":
            quality_val=90
            name=input("Dime el nombre con extension:")
            rotpic.save(name,quality=quality_val)
        elif yn=="n":
                print("Imagen no guardada")
    except:
        print("No se pudo realizar la operacion")

def _clipboard_copyC3(inst):
    def wrapperC3(event):
        """put colors in a L picture"""
        try:
            picL=img.convert("L")
            inst.clipboard_clear()
            seleccionC1=inst['text']
            coloriza = ImageOps.colorize(picL, seleccionC1, "black")
            coloriza.show()
            yn=input("Quieres guardar(s/n):")
            saveimg(yn,coloriza)
            print("Por favor, cierre la paleta de colores manualmente")
        except:
            print("No se pudo realizar la operacion")
            print("Por favor cierre la paleta de colores manualmente")
    return wrapperC3

def paste():
    """takes some pictures and paste them together"""
    try:
	    pic1=input("Escriba la ruta, el nombre y formato de la 1ra imagen a pegar:")
	    pic2=input("Escriba la ruta, el nombre y formato de la 2da imagen a pegar:")
	    img1=pic1.replace("\"","")
	    img2=pic2.replace("\"","")
	    imagen1 = Image.open(img1)
	    imagen2 = Image.open(img2)
	    witdh1,height1 = imagen1.size
	    witdh2,height2 = imagen2.size
	    print("1.Acostada\n2.parada")
	    opc2=input("Como deseas colocar la imagen")
	    if opc2 == "1":
	        if height1>height2:
	            tamano_height = height1
	        elif height2>height1:
	            tamano_height = height2
	        else:
	            tamano_height = height1
	        final = Image.new("RGB",(witdh1+witdh2,tamano_height),"black")
	        final.paste(imagen1,(0,0))
	        final.paste(imagen2,(witdh1,0))
	    if opc2 == "2":
	        if witdh1>witdh2:
	            tamano_witdh=witdh1
	        elif witdh2>witdh1:
	            tamano_witdh=witdh2
	        else:
	            tamano_witdh=witdh1
	        final = Image.new("RGB",(tamano_witdh,height1+height2),"black")
	        final.paste(imagen1,(0,0))
	        final.paste(imagen2,(0,height1))
	    final.show()
	    yn=input("Quieres guardar(s/n):")
	    saveimg(yn,final)
    except:
        print("No se pudo realizar la operacion")

def thumbnail(img):
    """takes a  picture an converts it to a thumbnail"""
    try:
	    miniatura = (160,120)
	    img.thumbnail(miniatura)
	    img.show()
	    yn=input("Quieres guardar(s/n):")
	    saveimg(yn,img)
    except:
        print("No se pudo realizar la operacion")

def _clipboard_copyT2(inst):
    def wrapperT2(event):
        """put a signature  in a picture"""
        try:
	        inst.clipboard_clear()
	        seleccionT=inst['text']
	        tex=input("Escriba el texto:")
	        siz=input("Dime el tamaño de letra:")
	        tam_text=len(tex)
	        print("Las fuentes disponibles son:")
	        for cosa in listdir("Fuentes"):
	            print(cosa)
	        fo=input("Escriba el nombre de la fuente:")
	        font="fuentes//"+fo
	        print("1.arriba izquierda\n2.abajo izquierda\n3.titulo\n4.personalizado")
	        pos=input("seleccione una posicion:")
	        img2 = img.convert("RGBA")#aqui
	        texto = Image.new('RGBA',img2.size,(255,255,255,0))
	        fuente = ImageFont.truetype(font,int(siz))
	        dibujo = ImageDraw.Draw(texto)
	        if pos == "1":
	            dibujo.text((0,0),tex,font=fuente,fill=seleccionT)
	        elif pos == "2":
	            dibujo.text((0,height-int(siz)),tex,font=fuente,fill=seleccionT)
	        elif pos == "3":
	            if witdh<=160:
	                dibujo.text((witdh/2-witdh/9,0),tex,font=fuente,fill=seleccionT)
	            elif witdh<=300:
	                dibujo.text((witdh/2-witdh/6,0),tex,font=fuente,fill=seleccionT)
	            elif witdh<=600:
	                dibujo.text((witdh/2-witdh/5,0),tex,font=fuente,fill=seleccionT)
	            elif witdh<=1024:
	                dibujo.text((witdh/2-witdh/10*tam_text*5,0),tex,font=fuente,fill=seleccionT)
	            elif witdh<=1700:
	                dibujo.text((witdh/2-witdh/6,0),tex,font=fuente,fill=seleccionT)
	            elif witdh>2500:
	                dibujo.text((witdh/2-witdh/5-tam_text*5,0),tex,font=fuente,fill=seleccionT)
	        elif pos == "4":
	            print(img2.size)
	            wit=input("Seleccione el primer valor(0=izquierda,n=derecha):")
	            hei=input("Seleccione el segundo valor(0=arriba,n=abajo):")
	            dibujo.text((int(wit),int(hei)),tex,font=fuente,fill=seleccionT)
	        else:
	            print("Esa no vale")
	        final = Image.alpha_composite(img2,texto)
	        final.show()
	        yn=input("Quieres guardar(s/n):")
	        saveimg(yn,final)
	        print("Por favor cierre la paleta de colores manualmente")
        except:
            print("No se pudo realizar la operacion")
            print("Por favor cierre la paleta de colores manualmente")
    return wrapperT2

def Drawing(img):
    try:
        drawpic=ImageDraw.Draw(img)
        witdh,height=img.size
        tam=input("Que tamaño de letra usaras?")
        print("1.arriba\n2.abajo\n3.altura personalizada")
        lin=input("Seleccione una posicion:")
        if lin == "1":
            drawpic.line((0,int(tam)) + (witdh,int(tam)),fill=None)
        elif lin == "2":
            drawpic.line((0,height-int(tam))+(witdh,height-int(tam)),fill=None)
        elif lin == "3":
            alt=input("Elije la altura")
            drawpic.line((0,int(alt)) + (witdh,int(alt)),fill=None)
        else:
            print("Esa no vale")
        img.show()
        #derecha arriba/abajo + #izquierda arriba/abajo fill=tupla 3 numeros
    except:
        print("No se pudo realizar la operacion")

def _clipboard_copy(inst):
    def wrapper(event):
        try:
            tam=input("Dime el tamaño del borde:")
            inst.clipboard_clear()
            seleccion=inst['text']
            mode=img.mode
            if mode=="RGB" or mode == "P":
                imgborde = ImageOps.expand(img, border=int(tam), fill=seleccion)
            else:
                print("No puedo añadir bordes")
            imgborde.show()
            yn = input("Quieres guardar(s/n):")
            saveimg(yn,imgborde)
            print("Por favor cierre la paleta de colores manualmente")
        except:
            print("No se pudo realizar la operacion")
            print("Por favor cierre la paleta de colores manualmente")
    return wrapper

def convertmodes(img):
    """takes a picture and converts it"""
    try:
        print("""1.1\n2.L\n3.P\n4.RGB\n5.RGBA
    6.CMYK\n7.YCbCr\n8.LAB\n9.HSV\n10.I\n11.F\n12.LA\n13.RGBX\n14.RGBa""")
        h=input("Seleccione una opcion:")
        if h == "1":
            conpic = img.convert("1")
        elif h == "2":
            conpic = img.convert("L")
        elif h =="3":
            conpic= img.convert(mode="P",colors=16)
        elif h == "4":
            conpic= img.convert("RGB")
        elif h=="5":
            conpic= img.convert("RGBA")
        elif h == "6":
            conpic= img.convert("CMYK")
        elif h == "7":
            conpic= img.convert("YCbCr")
        elif h == "8":
            conpic= img.convert("LAB")
        elif h=="9":
            conpic= img.convert("HSV")
        elif h=="10":
            conpic= img.convert("I")
        elif h=="11":
            conpic= img.convert("F")
        elif h=="12":
            conpic= img.convert("LA")
        elif h=="13":
            conpic= img.convert("RGBX")
        elif h=="14":
            conpic= img.convert("RGBa")
        else:
            print("Esa no vale")
        print(conpic.mode)
        conpic.show()
        yn=input("Quieres guardar(s/n):")
        saveimg(yn,conpic)
    except:
        print("no se pudo realizar la operacion")

def black_and_white_less(img):
    """take an image and put it in black and white"""
    width, height = img.size
    gray_base = 180
    for w in range(width):
        for h in range(height):
            r, g, b = img.getpixel((w, h))
            gray = (r+g+b)/2
            if gray < gray_base:
                img.putpixel((w, h), (25, 25, 25))
            else:
                img.putpixel((w, h), (200, 200, 200))
    img.show()
    yn=input("Quieres guardar(s/n):")
    saveimg(yn,img)


def thresholds(img):
    """take an image and put it thresholds"""
    copy=img
    width, height = copy.size
    level_min = 100
    level_max = 200
    for w in range(width):
        for h in range(height):
            r, g, b = copy.getpixel((w, h))
            gray = (r+g+b)//3
            if gray < level_min:
                copy.putpixel((w, h), (0, 0, 0))
            elif gray > level_max:
                copy.putpixel((w, h), (255, 255, 255))
            else:
                copy.putpixel((w, h), (gray, gray, gray))
    copy.show()
    yn=input("Quieres guardar(s/n):")
    saveimg(yn,copy)

def thresholdsless(img):
    """take an image and put it thresholds less"""
    width, height = img.size
    level_min = 50
    level_max = 100
    for w in range(width):
        for h in range(height):
            r, g, b = img.getpixel((w, h))
            gray = (r+g+b)//3
            if gray < level_min:
                img.putpixel((w, h), (0, 0, 0))
            elif gray > level_max:
                img.putpixel((w, h), (255, 255, 255))
            else:
                img.putpixel((w, h), (gray, gray, gray))
    img.show()
    yn=input("Quieres guardar(s/n):")
    saveimg(yn,img)


def juno(img):
    """takes an image and put it"""
    width, height = img.size
    for w in range(width):
        for h in range(height):
            r, g, b = img.getpixel((w, h))
            pre=img.putpixel((w,h),(r,g+50,b+70))
    img.show()
    yn=input("Quieres guardar(s/n):")
    saveimg(yn,img)


def juno2(img):
    """takes an image and put it"""
    width, height = img.size
    copy = img
    for w in range(width):
        for h in range(height):
            r, g, b = img.getpixel((w, h))
            RD=r*2
            GD=g*2
            BD=b*2
            img.putpixel((w,h),(BD,BD,BD))
    img.show()
    yn=input("Quieres guardar(s/n):")
    saveimg(yn,img)


def average(img):
    """take an image and put it average"""
    width, height = img.size
    image_copy = img
    for w in range(width):
        for h in range(height):
            if w > 0 and w < width-1 and h > 0 and h < height-1:
                r1, g1, b1 = image_copy.getpixel((w, h))
                r2, g2, b2 = image_copy.getpixel((w, h-1))
                r3, g3, b3 = image_copy.getpixel((w-1, h))
                r4, g4, b4 = image_copy.getpixel((w, h+1))
                r5, g5, b5 = image_copy.getpixel((w+1, h))
                r, g, b = ((r1+r2+r3+r4+r5)//5,
                           (g1+g2+g3+g4+g5)//5,
                           (b1+b2+b3+b4+b5)//5)
                img.putpixel((w, h), (r, g, b))
    img.show()
    yn=input("Quieres guardar(s/n):")
    saveimg(yn,img)

def average_allneighbors(img):
    """take an image and put  it Average All Neighbors"""
    width, height = img.size
    image_copy = img
    for w in range(width):
        for h in range(height):
            if w > 0 and w < width-1 and h > 0 and h < height-1:
                r1, g1, b1 = image_copy.getpixel((w, h))
                r2, g2, b2 = image_copy.getpixel((w, h-1))
                r3, g3, b3 = image_copy.getpixel((w, h+1))
                r4, g4, b4 = image_copy.getpixel((w-1, h))
                r5, g5, b5 = image_copy.getpixel((w-1, h-1))
                r6, g6, b6 = image_copy.getpixel((w-1, h+1))
                r7, g7, b7 = image_copy.getpixel((w+1, h))
                r8, g8, b8 = image_copy.getpixel((w+1, h-1))
                r9, g9, b9 = image_copy.getpixel((w+1, h+1))
                r, g, b = ((r1+r2+r3+r4+r5+r6+r7+r8+r9)//9,
                           (g1+g2+g3+g4+g5+g6+g7+g8+g9)//9,
                           (b1+b2+b3+b4+b5+b6+b7+b8+b9)//9)
                img.putpixel((w, h), (r, g, b))
    img.show()
    yn=input("Quieres guardar(s/n):")
    saveimg(yn,img)

def sepia(img):
    """take an image and put it sepia"""
    width, height = img.size
    sepia_intensity = 25
    for w in range(width):
        for h in range(height):
            r, g, b = img.getpixel((w, h))
            gray = (r+g+b)//3
            r = gray + (sepia_intensity * 2)
            g = gray + sepia_intensity
            b = gray - sepia_intensity
            if r > 255:
                r = 255
            if g > 255:
                g = 255
            if b < 0:
                b = 0
            img.putpixel((w, h), (r, g, b))
    img.show()
    yn=input("Quieres guardar(s/n):")
    saveimg(yn,img)

def notgray(img):
    """take an image and put it sepia"""
    width, height = img.size
    sepia_intensity = 5
    for w in range(width):
        for h in range(height):
            r, g, b = img.getpixel((w, h))
            r = r + (sepia_intensity * 2)
            g = g + (sepia_intensity *2 )
            b = b - (sepia_intensity*2)
            img.putpixel((w, h), (r, g, b))
    img.show()
    yn=input("Quieres guardar(s/n):")
    saveimg(yn,img)

def sepiaDF(img):
    """take an image and put it sepia more"""
    width, height = img.size
    sepia_intensity = 5
    for w in range(width):
        for h in range(height):
            r, g, b = img.getpixel((w, h))
            gray = (r+g+b)//3
            r = gray + (sepia_intensity * 5)
            g = gray + sepia_intensity
            b = gray - sepia_intensity
            img.putpixel((w, h), (r+100, g+50, b))
    img.show()
    yn=input("Quieres guardar(s/n):")
    saveimg(yn,img)

def sepiaDFless(img):
    """take an image and put it sepia more"""
    width, height = img.size
    sepia_intensity = 10
    for w in range(width):
        for h in range(height):
            r, g, b = img.getpixel((w, h))
            gray = (r+g+b)//2
            r = gray + (sepia_intensity * 2)
            g = gray + sepia_intensity
            b = gray - sepia_intensity
            if r > 255:
                r = 200
            if g > 255:
                g = 200
            if b < 0:
                b = 0
            img.putpixel((w, h), (r, g, b))
    img.show()
    yn=input("Quieres guardar(s/n):")
    saveimg(yn,img)

def sepiaDFlessD(img):
    """take an image and put it sepia more"""
    width, height = img.size
    sepia_intensity = 10
    for w in range(width):
        for h in range(height):
            r, g, b = img.getpixel((w, h))
            gray = (r+g+b)//3
            r = gray + (sepia_intensity * 2)
            g = gray + sepia_intensity
            b = gray - sepia_intensity
            if r > 255:
                r = 200
            if g > 255:
                g = 200
            if b < 0:
                b = 0
            img.putpixel((w, h), (r, g, b))
    img.show()
    yn=input("Quieres guardar(s/n):")
    saveimg(yn,img)

def filterr(img):
    """takes a picture and puts a fliter on it"""
    try:
        print("""1.BLUR\t\t\t16.NEGATIVE LESS\t30.GINGHAM\n2.DETAIL\t\t17.NEGATIVE MORE\t31.ARTIC\n3.CONTOUR\t\t18.EQUALIZE\t\t32.DIBUJO\n4.EDGE_ENHANCE\t\t19.MORE BRIGHT\t\t33.CHARMES
5.EDGE_ENHANCE_MORE\t20.AUTOCONTRAST\n6.EMBOSS\t\t21.MORE CONTRAST\n7.FIND_EDGES\t\testos tardan un poco mas\n8.SMOOTH\t\t22.BLACK AND WHITE LESS
9.SMOOTH_MORE\t\t23.THRESHOLDS\n10.SHARPEN\t\t24.THRESHOLDS LESS\n11.SHARPEN MORE\t\t25.AVERAGE\n12.GRAYSCALE\t\t26.AVERAGE ALL NEGHBORS\n13.POSTERIZE\t\t27.OLD PICTURE
14.SOLARIZE\t\t28.ORANGE\n15.NEGATIVE\t\t29.VALENCIA""")
        i=input("Seleccione una opcion:")
        if i == "1":
            filpic=img.filter(ImageFilter.BLUR)
            filpic.show()
        elif i == "2":
            filpic=img.filter(ImageFilter.DETAIL)
            filpic.show()
        elif i == "3":
            filpic=img.filter(ImageFilter.CONTOUR)
            filpic.show()
        elif i == "4":
            filpic=img.filter(ImageFilter.EDGE_ENHANCE)
            filpic.show()
        elif i == "5":
            filpic= img.filter(ImageFilter.EDGE_ENHANCE_MORE)
            filpic.show()
        elif i == "6":
            filpic= img.filter(ImageFilter.EMBOSS)
            filpic.show()
        elif i == "7":
            filpic= img.filter(ImageFilter.FIND_EDGES)
            filpic.show()
        elif i == "8":
            filpic= img.filter(ImageFilter.SMOOTH)
            filpic.show()
        elif i == "9":
            filpic= img.filter(ImageFilter.SMOOTH_MORE)
            filpic.show()
        elif i == "10":
            filpic= img.filter(ImageFilter.SHARPEN)
            filpic.show()
        elif i == "11":
            filpic = ImageEnhance.Sharpness(img).enhance(9)
            filpic.show()
        elif i =="12":
            filpic= ImageOps.grayscale(img)
            filpic.show()
        elif i == "13":
            filpic= ImageOps.posterize(img,1)
            filpic.show()
        elif i == "14":
            filpic = ImageOps.solarize(img)
            filpic.show()
        elif i =="15":
            filpic = ImageOps.invert(img)
            filpic.show()
        elif i == "16":
            filpic = ImageEnhance.Contrast(img).enhance(-2)
            filpic.show()
        elif i == "17":
            filpic = ImageEnhance.Contrast(img).enhance(-7)
            filpic.show()
        elif i == "18":
            filpic= ImageOps.equalize(img)
            filpic.show()
        elif i == "19":
            filpic = ImageEnhance.Brightness(img).enhance(2)
            filpic.show()
        elif i =="20":
            filpic= ImageOps.autocontrast(img,cutoff=2,ignore=None)
            filpic.show()
        elif i == "21":
            filpic = ImageEnhance.Contrast(img).enhance(2)
            filpic.show()
        elif i == "22":
            black_and_white_less(img)
        elif i =="23":
            thresholds(img)
        elif i=="24":
            thresholdsless(img)
        elif i =="25":
            average(img)
        elif i =="26":
            average_allneighbors(img)
        elif i =="27":
            sepia(img)
        elif i =="28":
            sepiaDF(img)
        elif i == "29":
            sepiaDFlessD(img)
        elif i == "30":
            sepiaDFless(img)
        elif i == "31":
            print("Se puede mejorar añadiendo Contraste")
            juno(img)
        elif i == "32":
            juno2(img)
        elif i == "33":
            notgray(img)
        else:
            print("Esa no vale")
        if int(i) <=21 and int(i)!=0:
            yn=input("Quieres guardar(s/n):")
            saveimg(yn,filpic)
    except:
        print("No se pudo realizar la operacion")

def main(img):
    x=-1
    while x != 0:
        print("BIENVENIDOS AL SISTEMA MODIFICADOR DE IMAGENES")
        print("""\n1.information\n2.cortar\n3.mostrar canales(RGB)\n4.mezclar 1 imagen
5.cambiar tamaño\n6.voltear\n7.rotar\n8.convertir formato\n9.añadir filtro
10.thumbnail\n11.dibujar linea\n12.añadir borde\nLo siguiente requiere abrir la imagen de nuevo\n13.firmar\nLo siguiente trabaja con varias imagenes
14.mezclar dos o tres imagenes\n15.pegar dos imagenes\n16.agregar color\n0.salir""")
        x=input('Seleccione una opcion:')
        if x == "1":
            information(img)
        elif x == "2":
            cropp(img)
        elif x == "3":
            channels(img)
        elif x == "4":
            merge(img)
        elif x == "5":
            resize(img)
        elif x == "6":
            fliplr(img)
        elif x == "7":
            rotate(img)
        elif x == "8":
            convertmodes(img)
        elif x =="9":
            filterr(img)
        elif x =="10":
            thumbnail(img)
        elif x == "11":
            Drawing(img)
        elif x == "12":
            showcolors(COLORS)
        elif x == "13":
            showcolorsT2(COLORS)
        elif x == "14":
            merge2()
        elif x == "15":
            paste()
        elif x == "16":
            showcolorsC3(COLORS)
        elif x == "0":
            exit(0)
            img.close()
        else:
            print("Esa no vale")

if __name__=='__main__':
    main(img)
