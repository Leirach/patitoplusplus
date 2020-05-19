
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftCOMMAAND ASSIGN BOOL CHAR CLOSEBRAC CLOSEPAR COMMA CTEC CTEF CTEI CTES DESDE DETERM DIVIDE ENTONCES EQ FALSE FLOAT FUNCION GT GTE HACER HASTA HAZ ID INT INVERSE LCURLYB LT LTE MIENTRAS MINUS NEQ OPENBRAC OPENPAR OR PLUS PRINCIPAL PROGRAMA QUACKIN QUACKOUT RCURLYB RETORNO SEMICOLON SI SINO TIMES TRANSPOSE TRUE VAR VOIDprogram_declaration : PROGRAMA ID SEMICOLON declare_vars declare_func_rec declare_main OPENPAR CLOSEPAR bloque_funciondeclare_main : PRINCIPALdeclare_vars : VAR vars\n                    | emptyvars : var_id dimensions more_vars SEMICOLON vars\n            | emptyvar_id : tipo IDmore_vars : more_var_id dimensions more_vars\n                 | emptymore_var_id : COMMA IDdimensions : OPENBRAC CTEI CLOSEBRAC \n                  | OPENBRAC CTEI CLOSEBRAC OPENBRAC CTEI CLOSEBRAC\n                  | emptydeclare_func_rec : declare_func_rec declare_func\n                        | emptydeclare_func : FUNCION func_id OPENPAR declare_func_params CLOSEPAR bloque_funcionfunc_id : tipo ID\n               | VOID IDdeclare_func_params : get_func_params more_params\n                           | emptyget_func_params : tipo IDmore_params : more_var_id more_params\n                   | emptymore_var_id : COMMA tipo IDtipo : INT \n            | FLOAT\n            | CHAR\n            | BOOLbloque_funcion : LCURLYB declare_vars estatutos_rec RCURLYBbloque : LCURLYB estatutos_rec RCURLYBestatutos_rec : estatuto estatutos_rec\n                     | emptyestatuto : asignacion \n                | condicion \n                | func_void\n                | retorno\n                | escribe\n                | lee \n                | desde\n                | mientras_estatutoasignacion : id ASSIGN megaexp SEMICOLONcondicion : SI OPENPAR megaexp CLOSEPAR entonces bloque_entoncesentonces : ENTONCESbloque_entonces : bloque bloque_sinobloque_sino : sino bloque \n                   | emptysino : SINOfunc_void : func_call_id OPENPAR func_call_params CLOSEPAR SEMICOLONfunc_call_id : IDfunc_call_params : func_call_params COMMA func_call_params\n                        | emptyfunc_call_params : megaexpescribe : QUACKOUT OPENPAR print_options CLOSEPAR SEMICOLONprint_options : printable COMMA printableprint_options : printableprintable : megaexpprintable : CTESlee : QUACKIN OPENPAR ID read_more CLOSEPAR SEMICOLONread_more : COMMA ID read_more\n                 | emptyretorno : RETORNO OPENPAR megaexp CLOSEPAR SEMICOLONdesde : DESDE forId ASSIGN exp hasta exp hacer bloqueforId : IDhasta : HASTAhacer : HACERmientras_estatuto : mientras OPENPAR megaexp CLOSEPAR haz bloquemientras : MIENTRAShaz : HAZmegaexp : superexp\n               | megaexp boolean_op superexpsuperexp : exp\n                | superexp logical_op expexp : termino\n           | exp sums terminotermino : factor\n               | termino multdiv factorfactor : vcte\n              | openpar megaexp closeparfactor : unary_ops vcte\n              | unary_ops openpar megaexp closeparopenpar : OPENPARclosepar : CLOSEPARvcte : idid : ID\n          | ID OPENBRAC exp CLOSEBRAC\n          | ID OPENBRAC exp CLOSEBRAC OPENBRAC exp CLOSEBRACvcte : CTEIvcte : CTEFvcte : TRUE\n            | FALSEvcte : CTECboolean_op : OR \n                  | ANDlogical_op : GT\n                  | GTE\n                  | LT\n                  | LTE\n                  | NEQ\n                  | EQsums : MINUS \n            | PLUS multdiv : TIMES \n               | DIVIDE unary_ops : MINUS\n                 | PLUS\n                 | DETERM\n                 | TRANSPOSE\n                 | INVERSEempty :'
    
_lr_action_items = {'PROGRAMA':([0,],[2,]),'$end':([1,44,85,],[0,-1,-29,]),'ID':([2,6,7,10,12,13,14,15,16,17,28,29,33,39,42,45,49,50,54,62,64,65,66,67,68,69,70,71,79,87,88,89,90,91,92,93,96,104,105,111,112,113,114,115,116,129,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,150,153,156,158,172,174,175,179,180,181,185,186,187,188,192,193,195,201,202,203,],[3,-109,-4,-3,-6,25,-25,-26,-27,-28,37,38,41,-109,52,-109,59,-5,78,78,-33,-34,-35,-36,-37,-38,-39,-40,95,117,117,117,117,117,127,117,117,117,117,-81,-104,-105,-106,-107,-108,117,-41,117,-92,-93,117,-94,-95,-96,-97,-98,-99,117,-100,-101,117,-102,-103,117,117,117,178,-48,-61,-53,117,117,-64,-42,-109,78,-58,-66,-44,-46,-45,-30,-62,]),'SEMICOLON':([3,11,22,24,25,30,31,32,40,41,43,51,52,84,97,98,99,100,101,102,103,106,107,108,109,110,117,149,152,154,155,160,163,164,165,166,167,168,177,184,198,],[4,-109,-109,-13,-7,39,-109,-9,-109,-10,-11,-8,-24,-12,-83,131,-69,-71,-73,-75,-77,-87,-88,-89,-90,-91,-84,-79,172,174,175,-85,-70,-72,-74,-76,-78,-82,188,-80,-86,]),'VAR':([4,45,],[6,6,]),'PRINCIPAL':([4,5,6,7,8,9,10,12,19,39,50,82,85,],[-109,-109,-109,-4,20,-15,-3,-6,-14,-109,-5,-16,-29,]),'FUNCION':([4,5,6,7,8,9,10,12,19,39,50,82,85,],[-109,-109,-109,-4,21,-15,-3,-6,-14,-109,-5,-16,-29,]),'SI':([6,7,10,12,39,45,50,54,62,64,65,66,67,68,69,70,71,131,172,174,175,185,186,187,188,192,193,195,201,202,203,],[-109,-4,-3,-6,-109,-109,-5,73,73,-33,-34,-35,-36,-37,-38,-39,-40,-41,-48,-61,-53,-42,-109,73,-58,-66,-44,-46,-45,-30,-62,]),'RETORNO':([6,7,10,12,39,45,50,54,62,64,65,66,67,68,69,70,71,131,172,174,175,185,186,187,188,192,193,195,201,202,203,],[-109,-4,-3,-6,-109,-109,-5,75,75,-33,-34,-35,-36,-37,-38,-39,-40,-41,-48,-61,-53,-42,-109,75,-58,-66,-44,-46,-45,-30,-62,]),'QUACKOUT':([6,7,10,12,39,45,50,54,62,64,65,66,67,68,69,70,71,131,172,174,175,185,186,187,188,192,193,195,201,202,203,],[-109,-4,-3,-6,-109,-109,-5,76,76,-33,-34,-35,-36,-37,-38,-39,-40,-41,-48,-61,-53,-42,-109,76,-58,-66,-44,-46,-45,-30,-62,]),'QUACKIN':([6,7,10,12,39,45,50,54,62,64,65,66,67,68,69,70,71,131,172,174,175,185,186,187,188,192,193,195,201,202,203,],[-109,-4,-3,-6,-109,-109,-5,77,77,-33,-34,-35,-36,-37,-38,-39,-40,-41,-48,-61,-53,-42,-109,77,-58,-66,-44,-46,-45,-30,-62,]),'DESDE':([6,7,10,12,39,45,50,54,62,64,65,66,67,68,69,70,71,131,172,174,175,185,186,187,188,192,193,195,201,202,203,],[-109,-4,-3,-6,-109,-109,-5,79,79,-33,-34,-35,-36,-37,-38,-39,-40,-41,-48,-61,-53,-42,-109,79,-58,-66,-44,-46,-45,-30,-62,]),'MIENTRAS':([6,7,10,12,39,45,50,54,62,64,65,66,67,68,69,70,71,131,172,174,175,185,186,187,188,192,193,195,201,202,203,],[-109,-4,-3,-6,-109,-109,-5,81,81,-33,-34,-35,-36,-37,-38,-39,-40,-41,-48,-61,-53,-42,-109,81,-58,-66,-44,-46,-45,-30,-62,]),'RCURLYB':([6,7,10,12,39,45,50,54,61,62,63,64,65,66,67,68,69,70,71,86,131,172,174,175,185,186,187,188,192,193,195,197,201,202,203,],[-109,-4,-3,-6,-109,-109,-5,-109,85,-109,-32,-33,-34,-35,-36,-37,-38,-39,-40,-31,-41,-48,-61,-53,-42,-109,-109,-58,-66,-44,-46,202,-45,-30,-62,]),'INT':([6,21,33,36,39,],[14,14,14,14,14,]),'FLOAT':([6,21,33,36,39,],[15,15,15,15,15,]),'CHAR':([6,21,33,36,39,],[16,16,16,16,16,]),'BOOL':([6,21,33,36,39,],[17,17,17,17,17,]),'OPENBRAC':([11,25,31,41,43,52,78,117,160,],[23,-7,23,-10,53,-24,93,93,179,]),'COMMA':([11,22,24,25,31,40,41,43,47,52,57,59,84,89,97,99,100,101,102,103,106,107,108,109,110,117,119,120,121,124,125,126,127,149,153,160,163,164,165,166,167,168,173,178,184,198,],[-109,33,-13,-7,-109,33,-10,-11,33,-24,33,-21,-12,-109,-83,-69,-71,-73,-75,-77,-87,-88,-89,-90,-91,-84,153,-51,-52,156,-56,-57,158,-79,-109,-85,-70,-72,-74,-76,-78,-82,-50,158,-80,-86,]),'OPENPAR':([18,20,27,37,38,73,74,75,76,77,78,80,81,87,88,89,90,91,93,96,104,105,111,112,113,114,115,116,129,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,150,153,156,179,180,181,],[26,-2,36,-17,-18,88,89,90,91,92,-49,96,-67,111,111,111,111,111,111,111,111,111,-81,-104,-105,-106,-107,-108,111,111,-92,-93,111,-94,-95,-96,-97,-98,-99,111,-100,-101,111,-102,-103,111,111,111,111,111,-64,]),'VOID':([21,],[29,]),'CTEI':([23,53,87,88,89,90,91,93,96,104,105,111,112,113,114,115,116,129,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,150,153,156,179,180,181,],[34,60,106,106,106,106,106,106,106,106,106,-81,-104,-105,-106,-107,-108,106,106,-92,-93,106,-94,-95,-96,-97,-98,-99,106,-100,-101,106,-102,-103,106,106,106,106,106,-64,]),'CLOSEPAR':([26,36,41,46,47,48,52,56,57,58,59,83,89,97,99,100,101,102,103,106,107,108,109,110,117,118,119,120,121,122,123,124,125,126,127,130,148,149,153,157,159,160,163,164,165,166,167,168,169,173,176,178,184,189,198,],[35,-109,-10,55,-109,-20,-24,-19,-109,-23,-21,-22,-109,-83,-69,-71,-73,-75,-77,-87,-88,-89,-90,-91,-84,151,152,-51,-52,154,155,-55,-56,-57,-109,162,168,-79,-109,177,-60,-85,-70,-72,-74,-76,-78,-82,168,-50,-54,-109,-80,-59,-86,]),'CLOSEBRAC':([34,60,97,101,102,103,106,107,108,109,110,117,128,149,160,165,166,167,168,184,190,198,],[43,84,-83,-73,-75,-77,-87,-88,-89,-90,-91,-84,160,-79,-85,-74,-76,-78,-82,-80,198,-86,]),'LCURLYB':([35,55,170,171,182,183,194,196,199,200,],[45,45,187,-43,187,-68,187,-47,187,-65,]),'ASSIGN':([72,78,94,95,160,198,],[87,-84,129,-63,-85,-86,]),'CTEF':([87,88,89,90,91,93,96,104,105,111,112,113,114,115,116,129,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,150,153,156,179,180,181,],[107,107,107,107,107,107,107,107,107,-81,-104,-105,-106,-107,-108,107,107,-92,-93,107,-94,-95,-96,-97,-98,-99,107,-100,-101,107,-102,-103,107,107,107,107,107,-64,]),'TRUE':([87,88,89,90,91,93,96,104,105,111,112,113,114,115,116,129,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,150,153,156,179,180,181,],[108,108,108,108,108,108,108,108,108,-81,-104,-105,-106,-107,-108,108,108,-92,-93,108,-94,-95,-96,-97,-98,-99,108,-100,-101,108,-102,-103,108,108,108,108,108,-64,]),'FALSE':([87,88,89,90,91,93,96,104,105,111,112,113,114,115,116,129,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,150,153,156,179,180,181,],[109,109,109,109,109,109,109,109,109,-81,-104,-105,-106,-107,-108,109,109,-92,-93,109,-94,-95,-96,-97,-98,-99,109,-100,-101,109,-102,-103,109,109,109,109,109,-64,]),'CTEC':([87,88,89,90,91,93,96,104,105,111,112,113,114,115,116,129,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,150,153,156,179,180,181,],[110,110,110,110,110,110,110,110,110,-81,-104,-105,-106,-107,-108,110,110,-92,-93,110,-94,-95,-96,-97,-98,-99,110,-100,-101,110,-102,-103,110,110,110,110,110,-64,]),'MINUS':([87,88,89,90,91,93,96,97,100,101,102,103,104,106,107,108,109,110,111,117,128,129,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,149,150,153,156,160,161,164,165,166,167,168,179,180,181,184,190,191,198,],[112,112,112,112,112,112,112,-83,143,-73,-75,-77,112,-87,-88,-89,-90,-91,-81,-84,143,112,112,-92,-93,112,-94,-95,-96,-97,-98,-99,112,-100,-101,112,-102,-103,-79,112,112,112,-85,143,143,-74,-76,-78,-82,112,112,-64,-80,143,143,-86,]),'PLUS':([87,88,89,90,91,93,96,97,100,101,102,103,104,106,107,108,109,110,111,117,128,129,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,149,150,153,156,160,161,164,165,166,167,168,179,180,181,184,190,191,198,],[113,113,113,113,113,113,113,-83,144,-73,-75,-77,113,-87,-88,-89,-90,-91,-81,-84,144,113,113,-92,-93,113,-94,-95,-96,-97,-98,-99,113,-100,-101,113,-102,-103,-79,113,113,113,-85,144,144,-74,-76,-78,-82,113,113,-64,-80,144,144,-86,]),'DETERM':([87,88,89,90,91,93,96,104,111,129,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,150,153,156,179,180,181,],[114,114,114,114,114,114,114,114,-81,114,114,-92,-93,114,-94,-95,-96,-97,-98,-99,114,-100,-101,114,-102,-103,114,114,114,114,114,-64,]),'TRANSPOSE':([87,88,89,90,91,93,96,104,111,129,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,150,153,156,179,180,181,],[115,115,115,115,115,115,115,115,-81,115,115,-92,-93,115,-94,-95,-96,-97,-98,-99,115,-100,-101,115,-102,-103,115,115,115,115,115,-64,]),'INVERSE':([87,88,89,90,91,93,96,104,111,129,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,150,153,156,179,180,181,],[116,116,116,116,116,116,116,116,-81,116,116,-92,-93,116,-94,-95,-96,-97,-98,-99,116,-100,-101,116,-102,-103,116,116,116,116,116,-64,]),'CTES':([91,156,],[126,126,]),'TIMES':([97,101,102,103,106,107,108,109,110,117,149,160,165,166,167,168,184,198,],[-83,146,-75,-77,-87,-88,-89,-90,-91,-84,-79,-85,146,-76,-78,-82,-80,-86,]),'DIVIDE':([97,101,102,103,106,107,108,109,110,117,149,160,165,166,167,168,184,198,],[-83,147,-75,-77,-87,-88,-89,-90,-91,-84,-79,-85,147,-76,-78,-82,-80,-86,]),'GT':([97,99,100,101,102,103,106,107,108,109,110,117,149,160,163,164,165,166,167,168,184,198,],[-83,136,-71,-73,-75,-77,-87,-88,-89,-90,-91,-84,-79,-85,136,-72,-74,-76,-78,-82,-80,-86,]),'GTE':([97,99,100,101,102,103,106,107,108,109,110,117,149,160,163,164,165,166,167,168,184,198,],[-83,137,-71,-73,-75,-77,-87,-88,-89,-90,-91,-84,-79,-85,137,-72,-74,-76,-78,-82,-80,-86,]),'LT':([97,99,100,101,102,103,106,107,108,109,110,117,149,160,163,164,165,166,167,168,184,198,],[-83,138,-71,-73,-75,-77,-87,-88,-89,-90,-91,-84,-79,-85,138,-72,-74,-76,-78,-82,-80,-86,]),'LTE':([97,99,100,101,102,103,106,107,108,109,110,117,149,160,163,164,165,166,167,168,184,198,],[-83,139,-71,-73,-75,-77,-87,-88,-89,-90,-91,-84,-79,-85,139,-72,-74,-76,-78,-82,-80,-86,]),'NEQ':([97,99,100,101,102,103,106,107,108,109,110,117,149,160,163,164,165,166,167,168,184,198,],[-83,140,-71,-73,-75,-77,-87,-88,-89,-90,-91,-84,-79,-85,140,-72,-74,-76,-78,-82,-80,-86,]),'EQ':([97,99,100,101,102,103,106,107,108,109,110,117,149,160,163,164,165,166,167,168,184,198,],[-83,141,-71,-73,-75,-77,-87,-88,-89,-90,-91,-84,-79,-85,141,-72,-74,-76,-78,-82,-80,-86,]),'OR':([97,98,99,100,101,102,103,106,107,108,109,110,117,118,121,122,125,130,148,149,160,163,164,165,166,167,168,169,184,198,],[-83,133,-69,-71,-73,-75,-77,-87,-88,-89,-90,-91,-84,133,133,133,133,133,133,-79,-85,-70,-72,-74,-76,-78,-82,133,-80,-86,]),'AND':([97,98,99,100,101,102,103,106,107,108,109,110,117,118,121,122,125,130,148,149,160,163,164,165,166,167,168,169,184,198,],[-83,134,-69,-71,-73,-75,-77,-87,-88,-89,-90,-91,-84,134,134,134,134,134,134,-79,-85,-70,-72,-74,-76,-78,-82,134,-80,-86,]),'HASTA':([97,101,102,103,106,107,108,109,110,117,149,160,161,165,166,167,168,184,198,],[-83,-73,-75,-77,-87,-88,-89,-90,-91,-84,-79,-85,181,-74,-76,-78,-82,-80,-86,]),'HACER':([97,101,102,103,106,107,108,109,110,117,149,160,165,166,167,168,184,191,198,],[-83,-73,-75,-77,-87,-88,-89,-90,-91,-84,-79,-85,-74,-76,-78,-82,-80,200,-86,]),'ENTONCES':([151,],[171,]),'HAZ':([162,],[183,]),'SINO':([186,202,],[196,-30,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program_declaration':([0,],[1,]),'declare_vars':([4,45,],[5,54,]),'empty':([4,5,6,11,22,31,36,39,40,45,47,54,57,62,89,127,153,178,186,187,],[7,9,12,24,32,24,48,12,32,7,58,63,58,63,120,159,120,159,195,63,]),'declare_func_rec':([5,],[8,]),'vars':([6,39,],[10,50,]),'var_id':([6,39,],[11,11,]),'tipo':([6,21,33,36,39,],[13,28,42,49,13,]),'declare_main':([8,],[18,]),'declare_func':([8,],[19,]),'dimensions':([11,31,],[22,40,]),'func_id':([21,],[27,]),'more_vars':([22,40,],[30,51,]),'more_var_id':([22,40,47,57,],[31,31,57,57,]),'bloque_funcion':([35,55,],[44,82,]),'declare_func_params':([36,],[46,]),'get_func_params':([36,],[47,]),'more_params':([47,57,],[56,83,]),'estatutos_rec':([54,62,187,],[61,86,197,]),'estatuto':([54,62,187,],[62,62,62,]),'asignacion':([54,62,187,],[64,64,64,]),'condicion':([54,62,187,],[65,65,65,]),'func_void':([54,62,187,],[66,66,66,]),'retorno':([54,62,187,],[67,67,67,]),'escribe':([54,62,187,],[68,68,68,]),'lee':([54,62,187,],[69,69,69,]),'desde':([54,62,187,],[70,70,70,]),'mientras_estatuto':([54,62,187,],[71,71,71,]),'id':([54,62,87,88,89,90,91,93,96,104,105,129,132,135,142,145,150,153,156,179,180,187,],[72,72,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,72,]),'func_call_id':([54,62,187,],[74,74,74,]),'mientras':([54,62,187,],[80,80,80,]),'forId':([79,],[94,]),'megaexp':([87,88,89,90,91,96,104,150,153,156,],[98,118,121,122,125,130,148,169,121,125,]),'superexp':([87,88,89,90,91,96,104,132,150,153,156,],[99,99,99,99,99,99,99,163,99,99,99,]),'exp':([87,88,89,90,91,93,96,104,129,132,135,150,153,156,179,180,],[100,100,100,100,100,128,100,100,161,100,164,100,100,100,190,191,]),'termino':([87,88,89,90,91,93,96,104,129,132,135,142,150,153,156,179,180,],[101,101,101,101,101,101,101,101,101,101,101,165,101,101,101,101,101,]),'factor':([87,88,89,90,91,93,96,104,129,132,135,142,145,150,153,156,179,180,],[102,102,102,102,102,102,102,102,102,102,102,102,166,102,102,102,102,102,]),'vcte':([87,88,89,90,91,93,96,104,105,129,132,135,142,145,150,153,156,179,180,],[103,103,103,103,103,103,103,103,149,103,103,103,103,103,103,103,103,103,103,]),'openpar':([87,88,89,90,91,93,96,104,105,129,132,135,142,145,150,153,156,179,180,],[104,104,104,104,104,104,104,104,150,104,104,104,104,104,104,104,104,104,104,]),'unary_ops':([87,88,89,90,91,93,96,104,129,132,135,142,145,150,153,156,179,180,],[105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,]),'func_call_params':([89,153,],[119,173,]),'print_options':([91,],[123,]),'printable':([91,156,],[124,176,]),'boolean_op':([98,118,121,122,125,130,148,169,],[132,132,132,132,132,132,132,132,]),'logical_op':([99,163,],[135,135,]),'sums':([100,128,161,164,190,191,],[142,142,142,142,142,142,]),'multdiv':([101,165,],[145,145,]),'read_more':([127,178,],[157,189,]),'closepar':([148,169,],[167,184,]),'entonces':([151,],[170,]),'hasta':([161,],[180,]),'haz':([162,],[182,]),'bloque_entonces':([170,],[185,]),'bloque':([170,182,194,199,],[186,192,201,203,]),'bloque_sino':([186,],[193,]),'sino':([186,],[194,]),'hacer':([191,],[199,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program_declaration","S'",1,None,None,None),
  ('program_declaration -> PROGRAMA ID SEMICOLON declare_vars declare_func_rec declare_main OPENPAR CLOSEPAR bloque_funcion','program_declaration',9,'p_program_declaration','patitoParser.py',18),
  ('declare_main -> PRINCIPAL','declare_main',1,'p_declare_main','patitoParser.py',28),
  ('declare_vars -> VAR vars','declare_vars',2,'p_declare_vars','patitoParser.py',32),
  ('declare_vars -> empty','declare_vars',1,'p_declare_vars','patitoParser.py',33),
  ('vars -> var_id dimensions more_vars SEMICOLON vars','vars',5,'p_vars','patitoParser.py',36),
  ('vars -> empty','vars',1,'p_vars','patitoParser.py',37),
  ('var_id -> tipo ID','var_id',2,'p_var_id','patitoParser.py',41),
  ('more_vars -> more_var_id dimensions more_vars','more_vars',3,'p_more_vars','patitoParser.py',46),
  ('more_vars -> empty','more_vars',1,'p_more_vars','patitoParser.py',47),
  ('more_var_id -> COMMA ID','more_var_id',2,'p_more_var_id','patitoParser.py',50),
  ('dimensions -> OPENBRAC CTEI CLOSEBRAC','dimensions',3,'p_dimensions','patitoParser.py',55),
  ('dimensions -> OPENBRAC CTEI CLOSEBRAC OPENBRAC CTEI CLOSEBRAC','dimensions',6,'p_dimensions','patitoParser.py',56),
  ('dimensions -> empty','dimensions',1,'p_dimensions','patitoParser.py',57),
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
  ('condicion -> SI OPENPAR megaexp CLOSEPAR entonces bloque_entonces','condicion',6,'p_condicion','patitoParser.py',123),
  ('entonces -> ENTONCES','entonces',1,'p_entonces','patitoParser.py',126),
  ('bloque_entonces -> bloque bloque_sino','bloque_entonces',2,'p_condicion_entonces','patitoParser.py',130),
  ('bloque_sino -> sino bloque','bloque_sino',2,'p_bloque_sino','patitoParser.py',133),
  ('bloque_sino -> empty','bloque_sino',1,'p_bloque_sino','patitoParser.py',134),
  ('sino -> SINO','sino',1,'p_condicion_sino','patitoParser.py',138),
  ('func_void -> func_call_id OPENPAR func_call_params CLOSEPAR SEMICOLON','func_void',5,'p_func_void','patitoParser.py',143),
  ('func_call_id -> ID','func_call_id',1,'p_func_call_id','patitoParser.py',147),
  ('func_call_params -> func_call_params COMMA func_call_params','func_call_params',3,'p_func_call_params','patitoParser.py',151),
  ('func_call_params -> empty','func_call_params',1,'p_func_call_params','patitoParser.py',152),
  ('func_call_params -> megaexp','func_call_params',1,'p_func_call_add_params','patitoParser.py',155),
  ('escribe -> QUACKOUT OPENPAR print_options CLOSEPAR SEMICOLON','escribe',5,'p_escribe','patitoParser.py',160),
  ('print_options -> printable COMMA printable','print_options',3,'p_print_multi','patitoParser.py',163),
  ('print_options -> printable','print_options',1,'p_print_single','patitoParser.py',165),
  ('printable -> megaexp','printable',1,'p_printable_exp','patitoParser.py',169),
  ('printable -> CTES','printable',1,'p_printable','patitoParser.py',171),
  ('lee -> QUACKIN OPENPAR ID read_more CLOSEPAR SEMICOLON','lee',6,'p_lee','patitoParser.py',180),
  ('read_more -> COMMA ID read_more','read_more',3,'p_read_more','patitoParser.py',183),
  ('read_more -> empty','read_more',1,'p_read_more','patitoParser.py',184),
  ('retorno -> RETORNO OPENPAR megaexp CLOSEPAR SEMICOLON','retorno',5,'p_retorno','patitoParser.py',188),
  ('desde -> DESDE forId ASSIGN exp hasta exp hacer bloque','desde',8,'p_desde','patitoParser.py',192),
  ('forId -> ID','forId',1,'p_forId','patitoParser.py',196),
  ('hasta -> HASTA','hasta',1,'p_desde_hasta','patitoParser.py',200),
  ('hacer -> HACER','hacer',1,'p_desde_hacer','patitoParser.py',204),
  ('mientras_estatuto -> mientras OPENPAR megaexp CLOSEPAR haz bloque','mientras_estatuto',6,'p_mientras_estatuto','patitoParser.py',209),
  ('mientras -> MIENTRAS','mientras',1,'p_mientras','patitoParser.py',214),
  ('haz -> HAZ','haz',1,'p_mientras_haz','patitoParser.py',219),
  ('megaexp -> superexp','megaexp',1,'p_megaexp','patitoParser.py',226),
  ('megaexp -> megaexp boolean_op superexp','megaexp',3,'p_megaexp','patitoParser.py',227),
  ('superexp -> exp','superexp',1,'p_superexp','patitoParser.py',233),
  ('superexp -> superexp logical_op exp','superexp',3,'p_superexp','patitoParser.py',234),
  ('exp -> termino','exp',1,'p_exp','patitoParser.py',240),
  ('exp -> exp sums termino','exp',3,'p_exp','patitoParser.py',241),
  ('termino -> factor','termino',1,'p_termino','patitoParser.py',247),
  ('termino -> termino multdiv factor','termino',3,'p_termino','patitoParser.py',248),
  ('factor -> vcte','factor',1,'p_factor','patitoParser.py',254),
  ('factor -> openpar megaexp closepar','factor',3,'p_factor','patitoParser.py',255),
  ('factor -> unary_ops vcte','factor',2,'p_factor_unary_op','patitoParser.py',258),
  ('factor -> unary_ops openpar megaexp closepar','factor',4,'p_factor_unary_op','patitoParser.py',259),
  ('openpar -> OPENPAR','openpar',1,'p_openpar','patitoParser.py',264),
  ('closepar -> CLOSEPAR','closepar',1,'p_closepar','patitoParser.py',269),
  ('vcte -> id','vcte',1,'p_vcte_ID','patitoParser.py',273),
  ('id -> ID','id',1,'p_id','patitoParser.py',281),
  ('id -> ID OPENBRAC exp CLOSEBRAC','id',4,'p_id','patitoParser.py',282),
  ('id -> ID OPENBRAC exp CLOSEBRAC OPENBRAC exp CLOSEBRAC','id',7,'p_id','patitoParser.py',283),
  ('vcte -> CTEI','vcte',1,'p_vcte_CTEI','patitoParser.py',287),
  ('vcte -> CTEF','vcte',1,'p_vcte_CTEF','patitoParser.py',294),
  ('vcte -> TRUE','vcte',1,'p_vcte_CTEB','patitoParser.py',301),
  ('vcte -> FALSE','vcte',1,'p_vcte_CTEB','patitoParser.py',302),
  ('vcte -> CTEC','vcte',1,'p_vcte_CTEC','patitoParser.py',309),
  ('boolean_op -> OR','boolean_op',1,'p_boolean_op','patitoParser.py',318),
  ('boolean_op -> AND','boolean_op',1,'p_boolean_op','patitoParser.py',319),
  ('logical_op -> GT','logical_op',1,'p_logical_op','patitoParser.py',324),
  ('logical_op -> GTE','logical_op',1,'p_logical_op','patitoParser.py',325),
  ('logical_op -> LT','logical_op',1,'p_logical_op','patitoParser.py',326),
  ('logical_op -> LTE','logical_op',1,'p_logical_op','patitoParser.py',327),
  ('logical_op -> NEQ','logical_op',1,'p_logical_op','patitoParser.py',328),
  ('logical_op -> EQ','logical_op',1,'p_logical_op','patitoParser.py',329),
  ('sums -> MINUS','sums',1,'p_sums','patitoParser.py',334),
  ('sums -> PLUS','sums',1,'p_sums','patitoParser.py',335),
  ('multdiv -> TIMES','multdiv',1,'p_multdiv','patitoParser.py',340),
  ('multdiv -> DIVIDE','multdiv',1,'p_multdiv','patitoParser.py',341),
  ('unary_ops -> MINUS','unary_ops',1,'p_unary_ops','patitoParser.py',346),
  ('unary_ops -> PLUS','unary_ops',1,'p_unary_ops','patitoParser.py',347),
  ('unary_ops -> DETERM','unary_ops',1,'p_unary_ops','patitoParser.py',348),
  ('unary_ops -> TRANSPOSE','unary_ops',1,'p_unary_ops','patitoParser.py',349),
  ('unary_ops -> INVERSE','unary_ops',1,'p_unary_ops','patitoParser.py',350),
  ('empty -> <empty>','empty',0,'p_empty','patitoParser.py',356),
]
