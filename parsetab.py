
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftCOMMAAND ASSIGN BOOL CHAR CLOSEBRAC CLOSEPAR COMMA CTEC CTEF CTEI CTES DESDE DETERM DIVIDE ENTONCES EQ FALSE FLOAT FUNCION GT GTE HACER HASTA HAZ ID INT INVERSE LCURLYB LT LTE MIENTRAS MINUS NEQ OPENBRAC OPENPAR OR PLUS PRINCIPAL PROGRAMA QUACKIN QUACKOUT RCURLYB RETORNO SEMICOLON SI SINO TIMES TRANSPOSE TRUE VAR VOIDprogram_declaration : PROGRAMA ID SEMICOLON declare_vars declare_func_rec declare_main OPENPAR CLOSEPAR bloque_funciondeclare_main : PRINCIPALdeclare_vars : VAR vars\n                    | emptyvars : first_var more_vars SEMICOLON vars\n            | emptyfirst_var : tipo ID dimensionsmore_vars : more_var_id more_vars\n                 | emptymore_var_id : COMMA ID dimensionsdimensions : emptydimensions : OPENBRAC CTEI CLOSEBRACdimensions : OPENBRAC CTEI CLOSEBRAC OPENBRAC CTEI CLOSEBRACdeclare_func_rec : declare_func_rec declare_func\n                        | emptydeclare_func : FUNCION func_id OPENPAR declare_func_params CLOSEPAR bloque_funcionfunc_id : tipo ID\n               | VOID IDdeclare_func_params : get_func_params more_params\n                           | emptyget_func_params : tipo IDmore_params : more_var_id more_params\n                   | emptymore_var_id : COMMA tipo IDtipo : INT \n            | FLOAT\n            | CHAR\n            | BOOLbloque_funcion : LCURLYB declare_vars estatutos_rec RCURLYBbloque : LCURLYB estatutos_rec RCURLYBestatutos_rec : estatuto estatutos_rec\n                     | emptyestatuto : asignacion \n                | condicion \n                | func_void\n                | retorno\n                | escribe\n                | lee \n                | desde\n                | mientras_estatutoasignacion : id ASSIGN megaexp SEMICOLONcondicion : SI OPENPAR megaexp CLOSEPAR entonces bloque_entoncesentonces : ENTONCESbloque_entonces : bloque bloque_sinobloque_sino : sino bloque \n                   | emptysino : SINOfunc_void : func_call_id OPENPAR func_call_params CLOSEPAR SEMICOLONfunc_call_id : IDfunc_call_params : func_call_params COMMA func_call_params\n                        | emptyfunc_call_params : megaexpescribe : QUACKOUT OPENPAR print_options CLOSEPAR SEMICOLONprint_options : print_options COMMA printable\n                     | printableprintable : megaexpprintable : CTESlee : QUACKIN OPENPAR read_options CLOSEPAR SEMICOLONread_options : read_options COMMA id\n                    | idretorno : RETORNO OPENPAR megaexp CLOSEPAR SEMICOLONdesde : DESDE id ASSIGN exp hasta exp hacer bloquehasta : HASTAhacer : HACERmientras_estatuto : mientras OPENPAR megaexp CLOSEPAR haz bloquemientras : MIENTRAShaz : HAZmegaexp : superexp\n               | megaexp boolean_op superexpsuperexp : exp\n                | superexp logical_op expexp : termino\n           | exp sums terminotermino : factor\n               | termino multdiv factorfactor : vcte\n              | openpar megaexp closeparfactor : unary_ops vcte\n              | unary_ops openpar megaexp closeparopenpar : OPENPARclosepar : CLOSEPARvcte : idid : IDid : ID OPENBRAC exp CLOSEBRACid : ID OPENBRAC exp CLOSEBRAC OPENBRAC exp CLOSEBRACvcte : CTEIvcte : CTEFvcte : TRUE\n            | FALSEvcte : CTECboolean_op : OR \n                  | ANDlogical_op : GT\n                  | GTE\n                  | LT\n                  | LTE\n                  | NEQ\n                  | EQsums : MINUS \n            | PLUS multdiv : TIMES \n               | DIVIDE unary_ops : MINUS\n                 | PLUS\n                 | DETERM\n                 | TRANSPOSE\n                 | INVERSEempty :'
    
_lr_action_items = {'PROGRAMA':([0,],[2,]),'$end':([1,46,84,],[0,-1,-29,]),'ID':([2,6,7,10,12,13,14,15,16,17,25,29,30,31,34,42,47,51,53,61,63,64,65,66,67,68,69,70,77,86,87,88,89,90,91,94,95,104,105,111,112,113,114,115,116,128,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,150,153,156,158,171,173,174,176,178,179,182,184,185,186,188,190,192,198,199,200,],[3,-108,-4,-3,-6,26,-25,-26,-27,-28,33,40,41,-108,44,-5,-108,58,79,79,-33,-34,-35,-36,-37,-38,-39,-40,93,93,93,93,93,93,93,93,93,93,93,-80,-103,-104,-105,-106,-107,93,-41,93,-91,-92,93,-93,-94,-95,-96,-97,-98,93,-99,-100,93,-101,-102,93,93,93,93,-48,-61,-53,-58,93,-63,93,-42,-108,79,-65,-44,-46,-45,-30,-62,]),'SEMICOLON':([3,11,22,23,24,26,32,33,35,36,43,44,52,93,96,97,98,99,100,101,102,103,106,107,108,109,110,149,152,154,155,157,161,162,163,164,165,166,167,183,197,],[4,-108,31,-108,-9,-108,-8,-108,-7,-11,-10,-24,-12,-83,-13,-82,131,-68,-70,-72,-74,-76,-86,-87,-88,-89,-90,-78,171,173,174,176,-84,-69,-71,-73,-75,-77,-81,-79,-85,]),'VAR':([4,47,],[6,6,]),'PRINCIPAL':([4,5,6,7,8,9,10,12,19,31,42,81,84,],[-108,-108,-108,-4,20,-15,-3,-6,-14,-108,-5,-16,-29,]),'FUNCION':([4,5,6,7,8,9,10,12,19,31,42,81,84,],[-108,-108,-108,-4,21,-15,-3,-6,-14,-108,-5,-16,-29,]),'SI':([6,7,10,12,31,42,47,53,61,63,64,65,66,67,68,69,70,131,171,173,174,176,184,185,186,188,190,192,198,199,200,],[-108,-4,-3,-6,-108,-5,-108,72,72,-33,-34,-35,-36,-37,-38,-39,-40,-41,-48,-61,-53,-58,-42,-108,72,-65,-44,-46,-45,-30,-62,]),'RETORNO':([6,7,10,12,31,42,47,53,61,63,64,65,66,67,68,69,70,131,171,173,174,176,184,185,186,188,190,192,198,199,200,],[-108,-4,-3,-6,-108,-5,-108,74,74,-33,-34,-35,-36,-37,-38,-39,-40,-41,-48,-61,-53,-58,-42,-108,74,-65,-44,-46,-45,-30,-62,]),'QUACKOUT':([6,7,10,12,31,42,47,53,61,63,64,65,66,67,68,69,70,131,171,173,174,176,184,185,186,188,190,192,198,199,200,],[-108,-4,-3,-6,-108,-5,-108,75,75,-33,-34,-35,-36,-37,-38,-39,-40,-41,-48,-61,-53,-58,-42,-108,75,-65,-44,-46,-45,-30,-62,]),'QUACKIN':([6,7,10,12,31,42,47,53,61,63,64,65,66,67,68,69,70,131,171,173,174,176,184,185,186,188,190,192,198,199,200,],[-108,-4,-3,-6,-108,-5,-108,76,76,-33,-34,-35,-36,-37,-38,-39,-40,-41,-48,-61,-53,-58,-42,-108,76,-65,-44,-46,-45,-30,-62,]),'DESDE':([6,7,10,12,31,42,47,53,61,63,64,65,66,67,68,69,70,131,171,173,174,176,184,185,186,188,190,192,198,199,200,],[-108,-4,-3,-6,-108,-5,-108,77,77,-33,-34,-35,-36,-37,-38,-39,-40,-41,-48,-61,-53,-58,-42,-108,77,-65,-44,-46,-45,-30,-62,]),'MIENTRAS':([6,7,10,12,31,42,47,53,61,63,64,65,66,67,68,69,70,131,171,173,174,176,184,185,186,188,190,192,198,199,200,],[-108,-4,-3,-6,-108,-5,-108,80,80,-33,-34,-35,-36,-37,-38,-39,-40,-41,-48,-61,-53,-58,-42,-108,80,-65,-44,-46,-45,-30,-62,]),'RCURLYB':([6,7,10,12,31,42,47,53,60,61,62,63,64,65,66,67,68,69,70,85,131,171,173,174,176,184,185,186,188,190,192,194,198,199,200,],[-108,-4,-3,-6,-108,-5,-108,-108,84,-108,-32,-33,-34,-35,-36,-37,-38,-39,-40,-31,-41,-48,-61,-53,-58,-42,-108,-108,-65,-44,-46,199,-45,-30,-62,]),'INT':([6,21,25,31,39,],[14,14,14,14,14,]),'FLOAT':([6,21,25,31,39,],[15,15,15,15,15,]),'CHAR':([6,21,25,31,39,],[16,16,16,16,16,]),'BOOL':([6,21,25,31,39,],[17,17,17,17,17,]),'COMMA':([11,23,26,33,35,36,43,44,49,52,56,58,88,93,96,97,99,100,101,102,103,106,107,108,109,110,118,119,120,122,123,124,125,126,127,149,153,161,162,163,164,165,166,167,172,175,177,183,197,],[25,25,-108,-108,-7,-11,-10,-24,25,-12,25,-21,-108,-83,-13,-82,-68,-70,-72,-74,-76,-86,-87,-88,-89,-90,153,-51,-52,156,-55,-56,-57,158,-60,-78,-108,-84,-69,-71,-73,-75,-77,-81,-50,-54,-59,-79,-85,]),'OPENPAR':([18,20,28,40,41,72,73,74,75,76,78,79,80,86,87,88,89,90,94,95,104,105,111,112,113,114,115,116,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,150,153,156,178,179,182,],[27,-2,39,-17,-18,87,88,89,90,91,94,-49,-66,111,111,111,111,111,111,111,111,111,-80,-103,-104,-105,-106,-107,111,111,-91,-92,111,-93,-94,-95,-96,-97,-98,111,-99,-100,111,-101,-102,111,111,111,111,-63,111,]),'VOID':([21,],[30,]),'OPENBRAC':([26,33,52,79,93,161,],[37,37,59,95,95,182,]),'CLOSEPAR':([27,33,36,39,43,44,48,49,50,52,55,56,57,58,82,88,93,96,97,99,100,101,102,103,106,107,108,109,110,117,118,119,120,121,122,123,124,125,126,127,129,148,149,153,161,162,163,164,165,166,167,168,172,175,177,183,197,],[38,-108,-11,-108,-10,-24,54,-108,-20,-12,-19,-108,-23,-21,-22,-108,-83,-13,-82,-68,-70,-72,-74,-76,-86,-87,-88,-89,-90,151,152,-51,-52,154,155,-55,-56,-57,157,-60,160,167,-78,-108,-84,-69,-71,-73,-75,-77,-81,167,-50,-54,-59,-79,-85,]),'CTEI':([37,59,86,87,88,89,90,94,95,104,105,111,112,113,114,115,116,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,150,153,156,178,179,182,],[45,83,106,106,106,106,106,106,106,106,106,-80,-103,-104,-105,-106,-107,106,106,-91,-92,106,-93,-94,-95,-96,-97,-98,106,-99,-100,106,-101,-102,106,106,106,106,-63,106,]),'LCURLYB':([38,54,169,170,180,181,191,193,195,196,],[47,47,186,-43,186,-67,186,-47,186,-64,]),'CLOSEBRAC':([45,83,93,97,101,102,103,106,107,108,109,110,130,149,161,164,165,166,167,183,189,197,],[52,96,-83,-82,-72,-74,-76,-86,-87,-88,-89,-90,161,-78,-84,-73,-75,-77,-81,-79,197,-85,]),'ASSIGN':([71,79,92,93,161,197,],[86,-83,128,-83,-84,-85,]),'CTEF':([86,87,88,89,90,94,95,104,105,111,112,113,114,115,116,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,150,153,156,178,179,182,],[107,107,107,107,107,107,107,107,107,-80,-103,-104,-105,-106,-107,107,107,-91,-92,107,-93,-94,-95,-96,-97,-98,107,-99,-100,107,-101,-102,107,107,107,107,-63,107,]),'TRUE':([86,87,88,89,90,94,95,104,105,111,112,113,114,115,116,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,150,153,156,178,179,182,],[108,108,108,108,108,108,108,108,108,-80,-103,-104,-105,-106,-107,108,108,-91,-92,108,-93,-94,-95,-96,-97,-98,108,-99,-100,108,-101,-102,108,108,108,108,-63,108,]),'FALSE':([86,87,88,89,90,94,95,104,105,111,112,113,114,115,116,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,150,153,156,178,179,182,],[109,109,109,109,109,109,109,109,109,-80,-103,-104,-105,-106,-107,109,109,-91,-92,109,-93,-94,-95,-96,-97,-98,109,-99,-100,109,-101,-102,109,109,109,109,-63,109,]),'CTEC':([86,87,88,89,90,94,95,104,105,111,112,113,114,115,116,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,150,153,156,178,179,182,],[110,110,110,110,110,110,110,110,110,-80,-103,-104,-105,-106,-107,110,110,-91,-92,110,-93,-94,-95,-96,-97,-98,110,-99,-100,110,-101,-102,110,110,110,110,-63,110,]),'MINUS':([86,87,88,89,90,93,94,95,97,100,101,102,103,104,106,107,108,109,110,111,128,130,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,149,150,153,156,159,161,163,164,165,166,167,178,179,182,183,187,189,197,],[112,112,112,112,112,-83,112,112,-82,143,-72,-74,-76,112,-86,-87,-88,-89,-90,-80,112,143,112,-91,-92,112,-93,-94,-95,-96,-97,-98,112,-99,-100,112,-101,-102,-78,112,112,112,143,-84,143,-73,-75,-77,-81,112,-63,112,-79,143,143,-85,]),'PLUS':([86,87,88,89,90,93,94,95,97,100,101,102,103,104,106,107,108,109,110,111,128,130,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,149,150,153,156,159,161,163,164,165,166,167,178,179,182,183,187,189,197,],[113,113,113,113,113,-83,113,113,-82,144,-72,-74,-76,113,-86,-87,-88,-89,-90,-80,113,144,113,-91,-92,113,-93,-94,-95,-96,-97,-98,113,-99,-100,113,-101,-102,-78,113,113,113,144,-84,144,-73,-75,-77,-81,113,-63,113,-79,144,144,-85,]),'DETERM':([86,87,88,89,90,94,95,104,111,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,150,153,156,178,179,182,],[114,114,114,114,114,114,114,114,-80,114,114,-91,-92,114,-93,-94,-95,-96,-97,-98,114,-99,-100,114,-101,-102,114,114,114,114,-63,114,]),'TRANSPOSE':([86,87,88,89,90,94,95,104,111,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,150,153,156,178,179,182,],[115,115,115,115,115,115,115,115,-80,115,115,-91,-92,115,-93,-94,-95,-96,-97,-98,115,-99,-100,115,-101,-102,115,115,115,115,-63,115,]),'INVERSE':([86,87,88,89,90,94,95,104,111,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,150,153,156,178,179,182,],[116,116,116,116,116,116,116,116,-80,116,116,-91,-92,116,-93,-94,-95,-96,-97,-98,116,-99,-100,116,-101,-102,116,116,116,116,-63,116,]),'CTES':([90,156,],[125,125,]),'TIMES':([93,97,101,102,103,106,107,108,109,110,149,161,164,165,166,167,183,197,],[-83,-82,146,-74,-76,-86,-87,-88,-89,-90,-78,-84,146,-75,-77,-81,-79,-85,]),'DIVIDE':([93,97,101,102,103,106,107,108,109,110,149,161,164,165,166,167,183,197,],[-83,-82,147,-74,-76,-86,-87,-88,-89,-90,-78,-84,147,-75,-77,-81,-79,-85,]),'GT':([93,97,99,100,101,102,103,106,107,108,109,110,149,161,162,163,164,165,166,167,183,197,],[-83,-82,136,-70,-72,-74,-76,-86,-87,-88,-89,-90,-78,-84,136,-71,-73,-75,-77,-81,-79,-85,]),'GTE':([93,97,99,100,101,102,103,106,107,108,109,110,149,161,162,163,164,165,166,167,183,197,],[-83,-82,137,-70,-72,-74,-76,-86,-87,-88,-89,-90,-78,-84,137,-71,-73,-75,-77,-81,-79,-85,]),'LT':([93,97,99,100,101,102,103,106,107,108,109,110,149,161,162,163,164,165,166,167,183,197,],[-83,-82,138,-70,-72,-74,-76,-86,-87,-88,-89,-90,-78,-84,138,-71,-73,-75,-77,-81,-79,-85,]),'LTE':([93,97,99,100,101,102,103,106,107,108,109,110,149,161,162,163,164,165,166,167,183,197,],[-83,-82,139,-70,-72,-74,-76,-86,-87,-88,-89,-90,-78,-84,139,-71,-73,-75,-77,-81,-79,-85,]),'NEQ':([93,97,99,100,101,102,103,106,107,108,109,110,149,161,162,163,164,165,166,167,183,197,],[-83,-82,140,-70,-72,-74,-76,-86,-87,-88,-89,-90,-78,-84,140,-71,-73,-75,-77,-81,-79,-85,]),'EQ':([93,97,99,100,101,102,103,106,107,108,109,110,149,161,162,163,164,165,166,167,183,197,],[-83,-82,141,-70,-72,-74,-76,-86,-87,-88,-89,-90,-78,-84,141,-71,-73,-75,-77,-81,-79,-85,]),'OR':([93,97,98,99,100,101,102,103,106,107,108,109,110,117,120,121,124,129,148,149,161,162,163,164,165,166,167,168,183,197,],[-83,-82,133,-68,-70,-72,-74,-76,-86,-87,-88,-89,-90,133,133,133,133,133,133,-78,-84,-69,-71,-73,-75,-77,-81,133,-79,-85,]),'AND':([93,97,98,99,100,101,102,103,106,107,108,109,110,117,120,121,124,129,148,149,161,162,163,164,165,166,167,168,183,197,],[-83,-82,134,-68,-70,-72,-74,-76,-86,-87,-88,-89,-90,134,134,134,134,134,134,-78,-84,-69,-71,-73,-75,-77,-81,134,-79,-85,]),'HASTA':([93,97,101,102,103,106,107,108,109,110,149,159,161,164,165,166,167,183,197,],[-83,-82,-72,-74,-76,-86,-87,-88,-89,-90,-78,179,-84,-73,-75,-77,-81,-79,-85,]),'HACER':([93,97,101,102,103,106,107,108,109,110,149,161,164,165,166,167,183,187,197,],[-83,-82,-72,-74,-76,-86,-87,-88,-89,-90,-78,-84,-73,-75,-77,-81,-79,196,-85,]),'ENTONCES':([151,],[170,]),'HAZ':([160,],[181,]),'SINO':([185,199,],[193,-30,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program_declaration':([0,],[1,]),'declare_vars':([4,47,],[5,53,]),'empty':([4,5,6,11,23,26,31,33,39,47,49,53,56,61,88,153,185,186,],[7,9,12,24,24,36,12,36,50,7,57,62,57,62,119,119,192,62,]),'declare_func_rec':([5,],[8,]),'vars':([6,31,],[10,42,]),'first_var':([6,31,],[11,11,]),'tipo':([6,21,25,31,39,],[13,29,34,13,51,]),'declare_main':([8,],[18,]),'declare_func':([8,],[19,]),'more_vars':([11,23,],[22,32,]),'more_var_id':([11,23,49,56,],[23,23,56,56,]),'func_id':([21,],[28,]),'dimensions':([26,33,],[35,43,]),'bloque_funcion':([38,54,],[46,81,]),'declare_func_params':([39,],[48,]),'get_func_params':([39,],[49,]),'more_params':([49,56,],[55,82,]),'estatutos_rec':([53,61,186,],[60,85,194,]),'estatuto':([53,61,186,],[61,61,61,]),'asignacion':([53,61,186,],[63,63,63,]),'condicion':([53,61,186,],[64,64,64,]),'func_void':([53,61,186,],[65,65,65,]),'retorno':([53,61,186,],[66,66,66,]),'escribe':([53,61,186,],[67,67,67,]),'lee':([53,61,186,],[68,68,68,]),'desde':([53,61,186,],[69,69,69,]),'mientras_estatuto':([53,61,186,],[70,70,70,]),'id':([53,61,77,86,87,88,89,90,91,94,95,104,105,128,132,135,142,145,150,153,156,158,178,182,186,],[71,71,92,97,97,97,97,97,127,97,97,97,97,97,97,97,97,97,97,97,97,177,97,97,71,]),'func_call_id':([53,61,186,],[73,73,73,]),'mientras':([53,61,186,],[78,78,78,]),'megaexp':([86,87,88,89,90,94,104,150,153,156,],[98,117,120,121,124,129,148,168,120,124,]),'superexp':([86,87,88,89,90,94,104,132,150,153,156,],[99,99,99,99,99,99,99,162,99,99,99,]),'exp':([86,87,88,89,90,94,95,104,128,132,135,150,153,156,178,182,],[100,100,100,100,100,100,130,100,159,100,163,100,100,100,187,189,]),'termino':([86,87,88,89,90,94,95,104,128,132,135,142,150,153,156,178,182,],[101,101,101,101,101,101,101,101,101,101,101,164,101,101,101,101,101,]),'factor':([86,87,88,89,90,94,95,104,128,132,135,142,145,150,153,156,178,182,],[102,102,102,102,102,102,102,102,102,102,102,102,165,102,102,102,102,102,]),'vcte':([86,87,88,89,90,94,95,104,105,128,132,135,142,145,150,153,156,178,182,],[103,103,103,103,103,103,103,103,149,103,103,103,103,103,103,103,103,103,103,]),'openpar':([86,87,88,89,90,94,95,104,105,128,132,135,142,145,150,153,156,178,182,],[104,104,104,104,104,104,104,104,150,104,104,104,104,104,104,104,104,104,104,]),'unary_ops':([86,87,88,89,90,94,95,104,128,132,135,142,145,150,153,156,178,182,],[105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,]),'func_call_params':([88,153,],[118,172,]),'print_options':([90,],[122,]),'printable':([90,156,],[123,175,]),'read_options':([91,],[126,]),'boolean_op':([98,117,120,121,124,129,148,168,],[132,132,132,132,132,132,132,132,]),'logical_op':([99,162,],[135,135,]),'sums':([100,130,159,163,187,189,],[142,142,142,142,142,142,]),'multdiv':([101,164,],[145,145,]),'closepar':([148,168,],[166,183,]),'entonces':([151,],[169,]),'hasta':([159,],[178,]),'haz':([160,],[180,]),'bloque_entonces':([169,],[184,]),'bloque':([169,180,191,195,],[185,188,198,200,]),'bloque_sino':([185,],[190,]),'sino':([185,],[191,]),'hacer':([187,],[195,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program_declaration","S'",1,None,None,None),
  ('program_declaration -> PROGRAMA ID SEMICOLON declare_vars declare_func_rec declare_main OPENPAR CLOSEPAR bloque_funcion','program_declaration',9,'p_program_declaration','patitoParser.py',18),
  ('declare_main -> PRINCIPAL','declare_main',1,'p_declare_main','patitoParser.py',22),
  ('declare_vars -> VAR vars','declare_vars',2,'p_declare_vars','patitoParser.py',26),
  ('declare_vars -> empty','declare_vars',1,'p_declare_vars','patitoParser.py',27),
  ('vars -> first_var more_vars SEMICOLON vars','vars',4,'p_vars','patitoParser.py',30),
  ('vars -> empty','vars',1,'p_vars','patitoParser.py',31),
  ('first_var -> tipo ID dimensions','first_var',3,'p_first_var','patitoParser.py',34),
  ('more_vars -> more_var_id more_vars','more_vars',2,'p_more_vars','patitoParser.py',39),
  ('more_vars -> empty','more_vars',1,'p_more_vars','patitoParser.py',40),
  ('more_var_id -> COMMA ID dimensions','more_var_id',3,'p_more_var_id','patitoParser.py',43),
  ('dimensions -> empty','dimensions',1,'p_dimensions_empty','patitoParser.py',47),
  ('dimensions -> OPENBRAC CTEI CLOSEBRAC','dimensions',3,'p_dimensions_one','patitoParser.py',51),
  ('dimensions -> OPENBRAC CTEI CLOSEBRAC OPENBRAC CTEI CLOSEBRAC','dimensions',6,'p_dimensions_two','patitoParser.py',55),
  ('declare_func_rec -> declare_func_rec declare_func','declare_func_rec',2,'p_declare_func_rec','patitoParser.py',60),
  ('declare_func_rec -> empty','declare_func_rec',1,'p_declare_func_rec','patitoParser.py',61),
  ('declare_func -> FUNCION func_id OPENPAR declare_func_params CLOSEPAR bloque_funcion','declare_func',6,'p_declare_func','patitoParser.py',64),
  ('func_id -> tipo ID','func_id',2,'p_func_id','patitoParser.py',68),
  ('func_id -> VOID ID','func_id',2,'p_func_id','patitoParser.py',69),
  ('declare_func_params -> get_func_params more_params','declare_func_params',2,'p_declare_func_params','patitoParser.py',73),
  ('declare_func_params -> empty','declare_func_params',1,'p_declare_func_params','patitoParser.py',74),
  ('get_func_params -> tipo ID','get_func_params',2,'p_get_func_params','patitoParser.py',77),
  ('more_params -> more_var_id more_params','more_params',2,'p_more_params','patitoParser.py',81),
  ('more_params -> empty','more_params',1,'p_more_params','patitoParser.py',82),
  ('more_var_id -> COMMA tipo ID','more_var_id',3,'p_more_params_id','patitoParser.py',85),
  ('tipo -> INT','tipo',1,'p_tipo','patitoParser.py',89),
  ('tipo -> FLOAT','tipo',1,'p_tipo','patitoParser.py',90),
  ('tipo -> CHAR','tipo',1,'p_tipo','patitoParser.py',91),
  ('tipo -> BOOL','tipo',1,'p_tipo','patitoParser.py',92),
  ('bloque_funcion -> LCURLYB declare_vars estatutos_rec RCURLYB','bloque_funcion',4,'p_bloque_funcion','patitoParser.py',97),
  ('bloque -> LCURLYB estatutos_rec RCURLYB','bloque',3,'p_bloque','patitoParser.py',101),
  ('estatutos_rec -> estatuto estatutos_rec','estatutos_rec',2,'p_estatutos_rec','patitoParser.py',104),
  ('estatutos_rec -> empty','estatutos_rec',1,'p_estatutos_rec','patitoParser.py',105),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','patitoParser.py',108),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','patitoParser.py',109),
  ('estatuto -> func_void','estatuto',1,'p_estatuto','patitoParser.py',110),
  ('estatuto -> retorno','estatuto',1,'p_estatuto','patitoParser.py',111),
  ('estatuto -> escribe','estatuto',1,'p_estatuto','patitoParser.py',112),
  ('estatuto -> lee','estatuto',1,'p_estatuto','patitoParser.py',113),
  ('estatuto -> desde','estatuto',1,'p_estatuto','patitoParser.py',114),
  ('estatuto -> mientras_estatuto','estatuto',1,'p_estatuto','patitoParser.py',115),
  ('asignacion -> id ASSIGN megaexp SEMICOLON','asignacion',4,'p_asignacion','patitoParser.py',119),
  ('condicion -> SI OPENPAR megaexp CLOSEPAR entonces bloque_entonces','condicion',6,'p_condicion','patitoParser.py',124),
  ('entonces -> ENTONCES','entonces',1,'p_entonces','patitoParser.py',127),
  ('bloque_entonces -> bloque bloque_sino','bloque_entonces',2,'p_condicion_entonces','patitoParser.py',131),
  ('bloque_sino -> sino bloque','bloque_sino',2,'p_bloque_sino','patitoParser.py',134),
  ('bloque_sino -> empty','bloque_sino',1,'p_bloque_sino','patitoParser.py',135),
  ('sino -> SINO','sino',1,'p_condicion_sino','patitoParser.py',139),
  ('func_void -> func_call_id OPENPAR func_call_params CLOSEPAR SEMICOLON','func_void',5,'p_func_void','patitoParser.py',144),
  ('func_call_id -> ID','func_call_id',1,'p_func_call_id','patitoParser.py',148),
  ('func_call_params -> func_call_params COMMA func_call_params','func_call_params',3,'p_func_call_params','patitoParser.py',152),
  ('func_call_params -> empty','func_call_params',1,'p_func_call_params','patitoParser.py',153),
  ('func_call_params -> megaexp','func_call_params',1,'p_func_call_add_params','patitoParser.py',156),
  ('escribe -> QUACKOUT OPENPAR print_options CLOSEPAR SEMICOLON','escribe',5,'p_escribe','patitoParser.py',161),
  ('print_options -> print_options COMMA printable','print_options',3,'p_print_multi','patitoParser.py',164),
  ('print_options -> printable','print_options',1,'p_print_multi','patitoParser.py',165),
  ('printable -> megaexp','printable',1,'p_printable_exp','patitoParser.py',169),
  ('printable -> CTES','printable',1,'p_printable','patitoParser.py',171),
  ('lee -> QUACKIN OPENPAR read_options CLOSEPAR SEMICOLON','lee',5,'p_lee','patitoParser.py',180),
  ('read_options -> read_options COMMA id','read_options',3,'p_read_options','patitoParser.py',183),
  ('read_options -> id','read_options',1,'p_read_options','patitoParser.py',184),
  ('retorno -> RETORNO OPENPAR megaexp CLOSEPAR SEMICOLON','retorno',5,'p_retorno','patitoParser.py',189),
  ('desde -> DESDE id ASSIGN exp hasta exp hacer bloque','desde',8,'p_desde','patitoParser.py',193),
  ('hasta -> HASTA','hasta',1,'p_desde_hasta','patitoParser.py',197),
  ('hacer -> HACER','hacer',1,'p_desde_hacer','patitoParser.py',201),
  ('mientras_estatuto -> mientras OPENPAR megaexp CLOSEPAR haz bloque','mientras_estatuto',6,'p_mientras_estatuto','patitoParser.py',206),
  ('mientras -> MIENTRAS','mientras',1,'p_mientras','patitoParser.py',211),
  ('haz -> HAZ','haz',1,'p_mientras_haz','patitoParser.py',216),
  ('megaexp -> superexp','megaexp',1,'p_megaexp','patitoParser.py',223),
  ('megaexp -> megaexp boolean_op superexp','megaexp',3,'p_megaexp','patitoParser.py',224),
  ('superexp -> exp','superexp',1,'p_superexp','patitoParser.py',230),
  ('superexp -> superexp logical_op exp','superexp',3,'p_superexp','patitoParser.py',231),
  ('exp -> termino','exp',1,'p_exp','patitoParser.py',237),
  ('exp -> exp sums termino','exp',3,'p_exp','patitoParser.py',238),
  ('termino -> factor','termino',1,'p_termino','patitoParser.py',244),
  ('termino -> termino multdiv factor','termino',3,'p_termino','patitoParser.py',245),
  ('factor -> vcte','factor',1,'p_factor','patitoParser.py',251),
  ('factor -> openpar megaexp closepar','factor',3,'p_factor','patitoParser.py',252),
  ('factor -> unary_ops vcte','factor',2,'p_factor_unary_op','patitoParser.py',255),
  ('factor -> unary_ops openpar megaexp closepar','factor',4,'p_factor_unary_op','patitoParser.py',256),
  ('openpar -> OPENPAR','openpar',1,'p_openpar','patitoParser.py',261),
  ('closepar -> CLOSEPAR','closepar',1,'p_closepar','patitoParser.py',266),
  ('vcte -> id','vcte',1,'p_vcte_ID','patitoParser.py',270),
  ('id -> ID','id',1,'p_id','patitoParser.py',275),
  ('id -> ID OPENBRAC exp CLOSEBRAC','id',4,'p_id_dimensions_one','patitoParser.py',282),
  ('id -> ID OPENBRAC exp CLOSEBRAC OPENBRAC exp CLOSEBRAC','id',7,'p_id_dimensions_two','patitoParser.py',287),
  ('vcte -> CTEI','vcte',1,'p_vcte_CTEI','patitoParser.py',292),
  ('vcte -> CTEF','vcte',1,'p_vcte_CTEF','patitoParser.py',299),
  ('vcte -> TRUE','vcte',1,'p_vcte_CTEB','patitoParser.py',306),
  ('vcte -> FALSE','vcte',1,'p_vcte_CTEB','patitoParser.py',307),
  ('vcte -> CTEC','vcte',1,'p_vcte_CTEC','patitoParser.py',314),
  ('boolean_op -> OR','boolean_op',1,'p_boolean_op','patitoParser.py',330),
  ('boolean_op -> AND','boolean_op',1,'p_boolean_op','patitoParser.py',331),
  ('logical_op -> GT','logical_op',1,'p_logical_op','patitoParser.py',336),
  ('logical_op -> GTE','logical_op',1,'p_logical_op','patitoParser.py',337),
  ('logical_op -> LT','logical_op',1,'p_logical_op','patitoParser.py',338),
  ('logical_op -> LTE','logical_op',1,'p_logical_op','patitoParser.py',339),
  ('logical_op -> NEQ','logical_op',1,'p_logical_op','patitoParser.py',340),
  ('logical_op -> EQ','logical_op',1,'p_logical_op','patitoParser.py',341),
  ('sums -> MINUS','sums',1,'p_sums','patitoParser.py',346),
  ('sums -> PLUS','sums',1,'p_sums','patitoParser.py',347),
  ('multdiv -> TIMES','multdiv',1,'p_multdiv','patitoParser.py',352),
  ('multdiv -> DIVIDE','multdiv',1,'p_multdiv','patitoParser.py',353),
  ('unary_ops -> MINUS','unary_ops',1,'p_unary_ops','patitoParser.py',358),
  ('unary_ops -> PLUS','unary_ops',1,'p_unary_ops','patitoParser.py',359),
  ('unary_ops -> DETERM','unary_ops',1,'p_unary_ops','patitoParser.py',360),
  ('unary_ops -> TRANSPOSE','unary_ops',1,'p_unary_ops','patitoParser.py',361),
  ('unary_ops -> INVERSE','unary_ops',1,'p_unary_ops','patitoParser.py',362),
  ('empty -> <empty>','empty',0,'p_empty','patitoParser.py',368),
]
