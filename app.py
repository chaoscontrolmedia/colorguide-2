from flask import Flask, render_template

app = Flask(__name__)

class ColorsandEmotion:
    def __init__(self, color, emotion):
        self.color = color
        self.emotion = emotion

    def description(self):
        return(f"{self.color}: {self.emotion}")


class BlendMode:
    def __init__(self, blend, operation):
        self.blend = blend
        self.operation = operation

    def blenddescription(self):
        return(f"{self.blend}: {self.operation}")

class ColorGrade:
    def __init__(self, grade, effect):
        self.grade = grade
        self.effect = effect

    def gradedescription(self):
        return(f"{self.grade}: {self.effect}")



colorlist = [
    ColorsandEmotion('Blue', 'Loyalty,Practical, Calm, Wisdom, trust,relaxed'),
    ColorsandEmotion('Black', 'Power, Death, Authority, Sinister, Mystery, Hard to Manipulate'),
    ColorsandEmotion('Red', 'Warm, Romantic, Strength, Power, Energy, Passion, Danger-Too much red-irritate'),
    ColorsandEmotion('White', 'Purity, Innocence'),
    ColorsandEmotion('Green','Relaxing, Clearer vision, Relaxed,Nature,Healing' ),
    ColorsandEmotion('Yellow','Happy, Active, Irritating, Flashy, Optimism, Warm'),
    ColorsandEmotion('Purple', "Calm, Powerful, Authority, Wealth, Ambition, Elegance, doesn't care what others think"),
    ColorsandEmotion('Pink', 'Kindness, Innocence'),
    ColorsandEmotion('Silver', 'Calm, cool'),
    ColorsandEmotion('Orange', 'Energy, Creative'),
    ColorsandEmotion('Desaturated', 'Post-apocalyptic'),
    ColorsandEmotion('Saturated', 'Vibrant, Comedies'),
]


blend_modes=[
    BlendMode('Normal', 'Layers do not interact'),
    BlendMode('Dissolve', 'layer dissolves as transparency decreases'),
    BlendMode('Darken','Any layer or pixels darker than the top layer will show'),
    BlendMode('Lighten','Any pixels lighter than the top layer will show'),
    BlendMode('Pin Light', 'Mix of Darken and Lighten'),
    BlendMode('Hard Mix', 'Reduces colors down to basic colors(RGB, CMYK)'),
    BlendMode('Subtract',"Subtracts pixel amounts. Can't go below 0"),
    BlendMode('Hue','Changes root color'),
    BlendMode('Luminosity','Allows you to change colors without affecting color of entire picture.'),
    BlendMode('average', 'The average of the two images. The result is darker than the original images. Algorithm: (A+B)/2 )' ),
    BlendMode('color-burn' , 'Image B gets darker based on the luminance of A. Algorithm: darken B towards A. One of the special 8 blend modes.'),
    BlendMode('color-dodge', 'Image B gets brighter based on the luminance of A.Brightens image but keeps 100 percent blacks. One of the special 8 blend modes. Algorithm: brighten B towards A )' ),
    BlendMode('conjoint-over', 'Similar to the over operation, except that if a pixel is partially covered by both a and b, conjoint-over assumes a completely hides b. For instance, two polygons where a and b share some edges but a completely overlaps b. Normal over produces a slightly transparent seam here. Algorithm: A+B(1-a)/b, A if a>b )' ),
    BlendMode('copy' , 'Only shows image A. This is useful if you also set the mix or mask controls so that some of B can still be seen. Algorithm: A )' ),
    BlendMode('difference', 'How much the pixels differ. Blacks show if no difference present.Also used to align pixels. See also Absminus. One of the special 8 blend modes. Algorithm: abs(A-B)' ),
    BlendMode('Darker' ,'Color-More harsh version of darken.'),
    BlendMode('Lighter', 'Color-Lighter version of lighten.'),
    BlendMode('disjoint','over - Similar to the over operation, except that if a pixel is partially covered by both a and b, disjoint-over assumes the two objects do not overlap. For instance, two polygons that touch and share an edge. Normal over produces a slightly transparent seam here. Algorithm: A+B(1-a)/b, A+B if a+b< 1 )' ),
    BlendMode('divide' ,'Divides the values but stops two negative values from becoming a positive number. Algorithm: A/B, 0 if A < 0 and B < 0)'),
    BlendMode('exclusion' ,'A more photographic form of difference. Makes blacks disappear..Algorithm: A+B-2AB'),
    BlendMode('from' , 'Image A is subtracted from B. Algorithm: B-A'),
    BlendMode('geometric', 'Another way of averaging two images. Algorithm: 2AB/(A+B)' ),
    BlendMode('hard-light', 'Image B is lit up by a very bright and sharp light in the shape of image A. Adds faded contrast with a blurred image on top. Algorithm: multiply if A<.5, screen if A>.5'),
    BlendMode('hypot', 'Resembles the plus and screen operations. The result is not as bright as plus, but brighter than screen. Hypot works with values above 1. Algorithm: diagonal sqrt(A*A+B*B)'),
    BlendMode('in', 'Only shows the areas of image A that overlap with the alpha of B. See also In. Algorithm: Ab'),
    BlendMode('Linear', 'Burn-unlike color burn, does not keep 100% white. Harsher version of Darken.One of the special 8 blend modes.'),
    BlendMode('Linear Light',"doesn't let there be 100% white or black."),
    BlendMode('mask', 'This is the reverse of the in operation. Only shows the areas of image B that overlap with the alpha of A. Algorithm: Ba)'),
    BlendMode('matte', 'Premultiplied over. Use unpremultiplied images with this operation. See also Matte.)'),
    BlendMode('Algorithm','Aa+B(1-a) (unpremultiplied over)'),
    BlendMode('Max', 'Takes the maximum values of both images. See also Max. Algorithm: max(A,B)'),
    BlendMode('Min', 'Takes the minimum values of both images. See also Min. Algorithm: min(A,B)'),
    BlendMode('Minus', 'Subtracts B from A. Algorithm: A-B)'),
    BlendMode('Multiply','Multiplies the values but stops two negative values from becoming a positive number.Darkens, shows 100 percent blacks, hides everything 100% white. See also Multiply. Algorithm: AB, A if A < 0 and B < 0)'),
    BlendMode('Out','Only shows the areas of image A that do not overlap with the alpha of B. See also Out. Algorithm: A(1-b)'),
    BlendMode('Over','This is the default operation. Layers image A over B according to the alpha of image A. Algorithm: A+B(1-a)'),
    BlendMode('Overlay','Image A brightens image B. Algorithm: multiply if B<.5, screen if B>.5'),
    BlendMode('Plus' ,'The sum of image A and B. Note that the plus algorithm may result in pixel values higher than 1.0. See also Plus. Algorithm: A+B)' ),
    BlendMode('Screen', 'If A or B is less than or equal to 1 the screen, else use the maximum example. Similar to plus. See also Screen. Algorithm: A+B-AB if A and B between 0-1, else A if A>B else B)'),
    BlendMode('Soft-light','Image B is lit up. Similar to hard-light and overlay, but not as extreme. Algorithm: B(2A+(B(1-AB))) if AB <1, 2AB otherwise'),
    BlendMode('Stencil','This is the reverse of the out operation. Only shows the areas of image B that do not overlap with the alpha of A.'),
    BlendMode('Algorithm', 'B(1-a)'),
    BlendMode('Under','This is the reverse of the over operation. Layers image B over A according to the matte of image B. Algorithm: A(1-b)+B)'),
    BlendMode('Vivid', 'Light-Lets there be 100% white anfdd black.'),
    BlendMode('Xor', 'Shows both image A and B where the images do not overlap. Algorithm: A(1-b)+B(1-a)' ),


]







@app.route('/')
def colors_and_emotion():
    return render_template('colorandemotion.html', 
    colorlist=colorlist,
    length=len(colorlist),
    title='Colors and Emotions')



@app.route('/blendops')
def blendops():
    return render_template('blendops.html',
    blend_modes=blend_modes,
    title='Blend Modes')


if __name__ == "__main__":
    app.run(debug=True)