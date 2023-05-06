"""
https://jinh.kr/ 의 javascript 코드를 리펙토링 한 뒤
js2py을 이용하여 python 파일로 변환하였습니다.
"""

__all__ = ['translate']



from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['analyze_b', 'LANG_KO', 'LANG_EN', 'm'])
@Js
def PyJsHoisted_analyze_b_(lang, text, this, arguments, var=var):
    var = Scope({'lang':lang, 'text':text, 'this':this, 'arguments':arguments}, var)
    var.registers(['assemble', 'lang', 'j', 'pre_assemble', 'output', 'input', 'k', 'text', 'analyze_sub'])
    @Js
    def PyJsHoisted_analyze_sub_(key_set, input, this, arguments, var=var):
        var = Scope({'key_set':key_set, 'input':input, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'j', 'input', 'key_set'])
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('input').get('length')):
            #for JS loop
            var.put('j', Js(0.0))
            while (var.get('j')<var.get('key_set').get('length')):
                if (var.get('key_set').get(var.get('j')).get('1').get('length')==Js(2.0)):
                    if ((var.get('input').get(var.get('i'))==var.get('key_set').get(var.get('j')).get('1').get('0')) and (var.get('input').get((var.get('i')+Js(1.0)))==var.get('key_set').get(var.get('j')).get('1').get('1'))):
                        var.get('input').put(var.get('i'), var.get('key_set').get(var.get('j')).get('0'))
                        var.get('input').put((var.get('i')+Js(1.0)), Js(''))
                        break
                else:
                    if (var.get('input').get(var.get('i'))==var.get('key_set').get(var.get('j')).get('1')):
                        var.get('input').put(var.get('i'), var.get('key_set').get(var.get('j')).get('0'))
                        break
                # update
                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
            # update
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        return var.get('input')
    PyJsHoisted_analyze_sub_.func_name = 'analyze_sub'
    var.put('analyze_sub', PyJsHoisted_analyze_sub_)
    @Js
    def PyJsHoisted_pre_assemble_(lang, this, arguments, var=var):
        var = Scope({'lang':lang, 'this':this, 'arguments':arguments}, var)
        var.registers(['lang'])
        if (var.get('lang')==var.get('LANG_EN')):
            pass
        else:
            if (var.get('lang')==var.get('LANG_KO')):
                var.put('text', var.get('text').callprop('replace', JsRegExp('/([⠠⠨⠰])⠻/g'), Js('$1ᅥᆼ')).callprop('replace', JsRegExp('/⠐⠂/g'), Js(':')))
        var.put('text', var.get('text').callprop('replace', JsRegExp('/⠦⠄/g'), Js('(')).callprop('replace', JsRegExp('/⠠⠴/g'), Js(')')).callprop('replace', JsRegExp('/⠼/g'), Js('')).callprop('replace', JsRegExp('/⠸([⠭⠴]+)⠇/g'), Js('$1')))
    PyJsHoisted_pre_assemble_.func_name = 'pre_assemble'
    var.put('pre_assemble', PyJsHoisted_pre_assemble_)
    @Js
    def PyJsHoisted_assemble_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        @Js
        def PyJs_anonymous_1_(v, this, arguments, var=var):
            var = Scope({'v':v, 'this':this, 'arguments':arguments}, var)
            var.registers(['v'])
            return var.get('v').callprop('slice', (-Js(1.0))).callprop('toUpperCase')
        PyJs_anonymous_1_._set_name('anonymous')
        @Js
        def PyJs_anonymous_2_(v, this, arguments, var=var):
            var = Scope({'v':v, 'this':this, 'arguments':arguments}, var)
            var.registers(['v'])
            return var.get('v').callprop('substring', Js(10.0), var.get('v').get('length')).callprop('toUpperCase')
        PyJs_anonymous_2_._set_name('anonymous')
        def PyJs_LONG_5_(var=var):
            def PyJs_LONG_4_(var=var):
                def PyJs_LONG_3_(var=var):
                    return var.get('output').callprop('replace', JsRegExp('/⠀/g'), Js(' ')).callprop('replace', JsRegExp('/ᇁ\\s/g'), Js('. ')).callprop('replace', JsRegExp('/ᇁ$/g'), Js('. ')).callprop('replace', JsRegExp('/ᄅ\\s/g'), Js(', ')).callprop('replace', JsRegExp('/ᄅ$/g'), Js(', ')).callprop('replace', JsRegExp('/ᄉᇀ/g'), Js("'")).callprop('replace', JsRegExp('/ᇂᆺ/g'), Js("'")).callprop('replace', JsRegExp('/ᇀ\\s/g'), Js('?'))
                return PyJs_LONG_3_().callprop('replace', JsRegExp('/ᇀ$/g'), Js('?')).callprop('replace', JsRegExp('/ᆿ\\s/g'), Js('!')).callprop('replace', JsRegExp('/ᆿ$/g'), Js('!')).callprop('replace', JsRegExp('/([ᅡ-ᅵ])\\(붙임\\)ᆻ/g'), Js('$1예')).callprop('replace', JsRegExp('/([ᅣᅪᅮᅯ])\\(붙임\\)ᅢ/g'), Js('$1애')).callprop('replace', JsRegExp('/([ᄀ-ᄒ])\\(붙임\\)/g'), Js('$1ᅡ')).callprop('replace', JsRegExp('/ᄑᆻ/g'), Js('폐'))
            return PyJs_LONG_4_().callprop('replace', JsRegExp('/ᅮᅢ/g'), Js('ᅱ')).callprop('replace', JsRegExp('/ᅣᅢ/g'), Js('ᅤ')).callprop('replace', JsRegExp('/ᅯᅢ/g'), Js('ᅰ')).callprop('replace', JsRegExp('/ᅪᅢ/g'), Js('ᅫ')).callprop('replace', JsRegExp('/([ᅡ-ᅵ])ᅨ/g'), Js('$1ᆻ')).callprop('replace', JsRegExp('/([ᄀ-ᄒ])((?=[^ᅡ-ᅵ])|$)/g'), Js('$1ᅡ')).callprop('replace', JsRegExp('/([^ᄀ-ᄒ])(?=[ᅡ-ᅵ])/g'), Js('$1ᄋ')).callprop('replace', JsRegExp('/(^[ᅡ-ᅵ])/g'), Js('ᄋ$1'))
        var.put('output', PyJs_LONG_5_().callprop('replace', JsRegExp('/\\(cap\\)\\(cap\\)([a-z]*)(?=\\s)/g'), PyJs_anonymous_2_).callprop('replace', JsRegExp('/\\(cap\\)(.)/g'), PyJs_anonymous_1_))
    PyJsHoisted_assemble_.func_name = 'assemble'
    var.put('assemble', PyJsHoisted_assemble_)
    var.put('output', Js(''))
    var.put('text', var.get('text').callprop('replace', JsRegExp('/\\n|\\r/g'), Js('\ue20b\ue00a\ue20b')))
    if (var.get('lang')==var.get('LANG_KO')):
        var.get('pre_assemble')(var.get('LANG_KO'))
    if (var.get('lang')==var.get('LANG_EN')):
        var.get('pre_assemble')(var.get('LANG_EN'))
    var.put('input', var.get('text').callprop('split', Js('')))
    pass
    pass
    pass
    if (var.get('lang')==var.get('LANG_KO')):
        var.put('input', var.get('analyze_sub')(var.get('m').get('tranlyze').get('key_b').get('kr'), var.get('input')))
    else:
        if (var.get('lang')==var.get('LANG_EN')):
            if (var.get('localStorage').get('s_braille_en_grade2')==Js('true')):
                var.put('input', var.get('analyze_sub')(var.get('m').get('tranlyze').get('key_b').get('en2'), var.get('input')))
            var.put('input', var.get('analyze_sub')(var.get('m').get('tranlyze').get('key_b').get('en'), var.get('input')))
        else:
            if (var.get('lang')==var.get('LANG_JA')):
                var.put('input', var.get('analyze_sub')(var.get('m').get('tranlyze').get('key_b').get('jp'), var.get('input')))
    var.put('input', var.get('analyze_sub')(var.get('m').get('tranlyze').get('key_b').get('nm'), var.get('input')))
    var.put('output', var.get('input').callprop('join', Js('')).callprop('replace', JsRegExp('/\ue20b\ue00a\ue20b/g'), Js('\n')))
    var.get('assemble')()
    return var.get('output')
PyJsHoisted_analyze_b_.func_name = 'analyze_b'
var.put('analyze_b', PyJsHoisted_analyze_b_)
var.put('m', Js({'tranlyze':Js({'key':Js({}),'list':Js({})})}))
def PyJs_LONG_0_(var=var):
    return var.get('m').get('tranlyze').put('key_b', Js({'en2':Js([Js([Js('st'), Js('⠌')]), Js([Js('ar'), Js('⠜')]), Js([Js('and'), Js('⠯')]), Js([Js('for'), Js('⠿')]), Js([Js('of'), Js('⠷')]), Js([Js('the'), Js('⠮')]), Js([Js('with'), Js('⠾')]), Js([Js('-ing'), Js('⠬')]), Js([Js('-ble'), Js('⠼')]), Js([Js('ch'), Js('⠡')]), Js([Js('gh'), Js('⠣')]), Js([Js('sh'), Js('⠩')]), Js([Js('th'), Js('⠹')]), Js([Js('wh'), Js('⠱')]), Js([Js('ed'), Js('⠫')]), Js([Js('er'), Js('⠻')]), Js([Js('ou'), Js('⠳')]), Js([Js('ow'), Js('⠪')]), Js([Js('-ea-'), Js('⠂')]), Js([Js('-bb-'), Js('⠆')]), Js([Js('-cc-'), Js('⠒')]), Js([Js('-dd-'), Js('⠲')]), Js([Js('-en-'), Js('⠢')]), Js([Js('-ff-'), Js('⠖')]), Js([Js('-gg-'), Js('⠶')]), Js([Js('“'), Js('⠦')]), Js([Js('in'), Js('⠔')]), Js([Js('”'), Js('⠴')]), Js([Js('com-'), Js('⠤')])]),'en':Js([Js([Js('a'), Js('⠁')]), Js([Js('b'), Js('⠃')]), Js([Js('c'), Js('⠉')]), Js([Js('d'), Js('⠙')]), Js([Js('e'), Js('⠑')]), Js([Js('f'), Js('⠋')]), Js([Js('g'), Js('⠛')]), Js([Js('h'), Js('⠓')]), Js([Js('i'), Js('⠊')]), Js([Js('j'), Js('⠚')]), Js([Js('k'), Js('⠅')]), Js([Js('l'), Js('⠇')]), Js([Js('m'), Js('⠍')]), Js([Js('n'), Js('⠝')]), Js([Js('o'), Js('⠕')]), Js([Js('p'), Js('⠏')]), Js([Js('q'), Js('⠟')]), Js([Js('r'), Js('⠗')]), Js([Js('s'), Js('⠎')]), Js([Js('t'), Js('⠞')]), Js([Js('u'), Js('⠥')]), Js([Js('v'), Js('⠧')]), Js([Js('w'), Js('⠺')]), Js([Js('x'), Js('⠭')]), Js([Js('y'), Js('⠽')]), Js([Js('z'), Js('⠵')]), Js([Js('(cap)'), Js('⠠')]), Js([Js('␃'), Js('␃')])]),'kr':Js([Js([Js('가'), Js('⠫')]), Js([Js('사'), Js('⠇')]), Js([Js('것'), Js('⠸⠎')]), Js([Js('ᅥᆨ'), Js('⠹')]), Js([Js('ᅥᆫ'), Js('⠾')]), Js([Js('ᅥᆯ'), Js('⠞')]), Js([Js('ᅧᆫ'), Js('⠡')]), Js([Js('ᅧᆯ'), Js('⠳')]), Js([Js('ᅧᆼ'), Js('⠻')]), Js([Js('ᅩᆨ'), Js('⠭')]), Js([Js('ᅩᆫ'), Js('⠷')]), Js([Js('ᅩᆼ'), Js('⠿')]), Js([Js('ᅮᆫ'), Js('⠛')]), Js([Js('ᅮᆯ'), Js('⠯')]), Js([Js('ᅳᆫ'), Js('⠵')]), Js([Js('ᅳᆯ'), Js('⠮')]), Js([Js('ᅵᆫ'), Js('⠟')]), Js([Js('그래서'), Js('⠁⠎')]), Js([Js('그러나'), Js('⠁⠉')]), Js([Js('그러면'), Js('⠁⠒')]), Js([Js('그러므로'), Js('⠁⠢')]), Js([Js('그런데'), Js('⠁⠝')]), Js([Js('그리고'), Js('⠁⠥')]), Js([Js('그리하여'), Js('⠁⠱')]), Js([Js('ᄀ'), Js('⠈')]), Js([Js('ᄁ'), Js('⠠⠈')]), Js([Js('ᄂ'), Js('⠉')]), Js([Js('ᄃ'), Js('⠊')]), Js([Js('ᄄ'), Js('⠠⠊')]), Js([Js('ᄅ'), Js('⠐')]), Js([Js('ᄆ'), Js('⠑')]), Js([Js('ᄇ'), Js('⠘')]), Js([Js('ᄈ'), Js('⠠⠘')]), Js([Js('ᄉ'), Js('⠠')]), Js([Js('ᄊ'), Js('⠠⠠')]), Js([Js('ㅇ'), Js('⠛')]), Js([Js('ᄌ'), Js('⠨')]), Js([Js('ᄍ'), Js('⠠⠨')]), Js([Js('ᄎ'), Js('⠰')]), Js([Js('ᄏ'), Js('⠋')]), Js([Js('ᄐ'), Js('⠓')]), Js([Js('ᄑ'), Js('⠙')]), Js([Js('ᄒ'), Js('⠚')]), Js([Js('ᅡ'), Js('⠣')]), Js([Js('ᅢ'), Js('⠗')]), Js([Js('ᅣ'), Js('⠜')]), Js([Js('ᅤ'), Js('⠜⠗')]), Js([Js('ᅥ'), Js('⠎')]), Js([Js('ᅦ'), Js('⠝')]), Js([Js('ᅧ'), Js('⠱')]), Js([Js('ᅨ'), Js('⠌')]), Js([Js('ᅩ'), Js('⠥')]), Js([Js('ᅪ'), Js('⠧')]), Js([Js('ᅫ'), Js('⠧⠗')]), Js([Js('ᅬ'), Js('⠽')]), Js([Js('ᅭ'), Js('⠬')]), Js([Js('ᅮ'), Js('⠍')]), Js([Js('ᅯ'), Js('⠏')]), Js([Js('ᅰ'), Js('⠏⠗')]), Js([Js('ᅱ'), Js('⠍⠗')]), Js([Js('ᅲ'), Js('⠩')]), Js([Js('ᅳ'), Js('⠪')]), Js([Js('ᅴ'), Js('⠺')]), Js([Js('ᅵ'), Js('⠕')]), Js([Js('×'), Js('⠭')]), Js([Js('○'), Js('⠴')]), Js([Js('␃'), Js('␃')]), Js([Js('ᆨ'), Js('⠁')]), Js([Js('ᆩ'), Js('⠈⠈')]), Js([Js('ᆪ'), Js('⠈⠠')]), Js([Js('ᆫ'), Js('⠒')]), Js([Js('ᆬ'), Js('⠒⠅')]), Js([Js('ᆭ'), Js('⠒⠴')]), Js([Js('ᆮ'), Js('⠔')]), Js([Js('ᆯ'), Js('⠂')]), Js([Js('ᆰ'), Js('⠂⠁')]), Js([Js('ᆱ'), Js('⠂⠢')]), Js([Js('ᆲ'), Js('⠂⠃')]), Js([Js('ᆳ'), Js('⠂⠄')]), Js([Js('ᆴ'), Js('⠂⠦')]), Js([Js('ᆵ'), Js('⠂⠲')]), Js([Js('ᆶ'), Js('⠂⠴')]), Js([Js('ᆷ'), Js('⠢')]), Js([Js('ᆸ'), Js('⠃')]), Js([Js('ᆹ'), Js('⠃⠄')]), Js([Js('ᆺ'), Js('⠄')]), Js([Js('ᆼ'), Js('⠶')]), Js([Js('ᆽ'), Js('⠅')]), Js([Js('ᆾ'), Js('⠆')]), Js([Js('ᆿ'), Js('⠖')]), Js([Js('ᇀ'), Js('⠦')]), Js([Js('ᇁ'), Js('⠲')]), Js([Js('ᇂ'), Js('⠴')]), Js([Js('ㄱ'), Js('⠈')]), Js([Js('ㄲ'), Js('⠠⠈')]), Js([Js('ㄳ'), Js('⠈⠠')]), Js([Js('ㄴ'), Js('⠉')]), Js([Js('ㄵ'), Js('⠉⠨')]), Js([Js('ㄶ'), Js('⠉⠚')]), Js([Js('ㄷ'), Js('⠊')]), Js([Js('ㄸ'), Js('⠠⠊')]), Js([Js('ㄹ'), Js('⠐')]), Js([Js('ㄺ'), Js('⠐⠈')]), Js([Js('ㄻ'), Js('⠐⠑')]), Js([Js('ㄼ'), Js('⠐⠘')]), Js([Js('ㄽ'), Js('⠐⠠')]), Js([Js('ㄾ'), Js('⠐⠓')]), Js([Js('ㄿ'), Js('⠐⠙')]), Js([Js('ㅀ'), Js('⠐⠚')]), Js([Js('ㅁ'), Js('⠑')]), Js([Js('ㅂ'), Js('⠘')]), Js([Js('ㅃ'), Js('⠠⠘')]), Js([Js('ㅄ'), Js('⠘⠠')]), Js([Js('ㅅ'), Js('⠠')]), Js([Js('ㅆ'), Js('⠠⠠')]), Js([Js('ㅈ'), Js('⠨')]), Js([Js('ㅉ'), Js('⠠⠨')]), Js([Js('ㅊ'), Js('⠰')]), Js([Js('ㅋ'), Js('⠋')]), Js([Js('ㅌ'), Js('⠓')]), Js([Js('ㅍ'), Js('⠙')]), Js([Js('ㅎ'), Js('⠚')]), Js([Js('ㅏ'), Js('⠣')]), Js([Js('ㅐ'), Js('⠗')]), Js([Js('ㅑ'), Js('⠜')]), Js([Js('ㅒ'), Js('⠜⠗')]), Js([Js('ㅓ'), Js('⠎')]), Js([Js('ㅔ'), Js('⠝')]), Js([Js('ㅕ'), Js('⠱')]), Js([Js('ㅖ'), Js('⠌')]), Js([Js('ㅗ'), Js('⠥')]), Js([Js('ㅘ'), Js('⠧')]), Js([Js('ㅙ'), Js('⠧⠗')]), Js([Js('ㅚ'), Js('⠽')]), Js([Js('ㅛ'), Js('⠬')]), Js([Js('ㅜ'), Js('⠍')]), Js([Js('ㅝ'), Js('⠏')]), Js([Js('ㅞ'), Js('⠏⠗')]), Js([Js('ㅟ'), Js('⠍⠗')]), Js([Js('ㅠ'), Js('⠩')]), Js([Js('ㅡ'), Js('⠪')]), Js([Js('ㅢ'), Js('⠺')]), Js([Js('ㅣ'), Js('⠕')]), Js([Js('ᆻ'), Js('⠌')]), Js([Js('(붙임)'), Js('⠤')]), Js([Js(','), Js('⠐')]), Js([Js('.'), Js('⠲')]), Js([Js(':'), Js('⠐⠂')]), Js([Js('('), Js('⠦⠄')]), Js([Js(')'), Js('⠠⠴')]), Js([Js('‘'), Js('⠠⠦')]), Js([Js('’'), Js('⠴⠄')]), Js([Js("'"), Js('⠴⠄')])]),'nm':Js([Js([Js(' '), Js('⠀')]), Js([Js('(num)'), Js('⠼')]), Js([Js('0'), Js('⠚')]), Js([Js('1'), Js('⠁')]), Js([Js('2'), Js('⠃')]), Js([Js('3'), Js('⠉')]), Js([Js('4'), Js('⠙')]), Js([Js('5'), Js('⠑')]), Js([Js('6'), Js('⠋')]), Js([Js('7'), Js('⠛')]), Js([Js('8'), Js('⠓')]), Js([Js('9'), Js('⠊')]), Js([Js(','), Js('⠂')]), Js([Js('.'), Js('⠲')]), Js([Js(';'), Js('⠆')]), Js([Js(':'), Js('⠒')]), Js([Js('.'), Js('⠄')]), Js([Js('!'), Js('⠖')]), Js([Js('?'), Js('⠦')])])}))
PyJs_LONG_0_()
var.put('LANG_KO', Js(1.0))
var.put('LANG_EN', Js(2.0))
pass
pass


# Add lib to the module scope
translate = var.to_python()