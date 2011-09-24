import unittest
from analizer import DSLAnalizer
from parsers.crawley_dsl import Line
from parsers.simple_parser import SimpleParser

class DSLAnalizerTest(unittest.TestCase):

    def test_primeros_elementos(self):
        
	    self.assertEquals("return [x for x in PyQuery(html).query('p')[0]]", DSLAnalizer().parse(Line("first < tag:'p' => innerHTML", 0)), "pido el primer 'p' del html")
	    self.assertEquals("return [x for x in PyQuery(html).query('p')[0] + PyQuery(html).query('div')[0]]", DSLAnalizer().parse(Line("first < tag:['p','div'] => innerHTML", 0)), "pido el primer elemento con tag = p o tag = div")

	    self.assertEquals("return [x for x in PyQuery(html).query('#unid')[0]]", DSLAnalizer().parse(Line("first < id:'unID' => innerHTML", 0)), "pido el primer elemento que tiene id = unid")
	    self.assertEquals("return [x for x in PyQuery(html).query('#unid')[0] + PyQuery(html).query('#otroid')[0]]", DSLAnalizer().parse(Line("first < id:['unid','otroid'] => innerHTML", 0)), "pido el primer elemento con id = unid o id = otroid")
		
	    self.assertEquals("return [x for x in PyQuery(html).query('.mi-clase')[0]]", DSLAnalizer().parse(Line("first < class:'mi-clase' => innerHTML", 0)), "pido el primer elemento que tiene clase = mi-clase")
	    self.assertEquals("return [x for x in PyQuery(html).query('.mi-clase')[0] + PyQuery(html).query('.otra-clase')[0]]", DSLAnalizer().parse(Line("first < class:['mi-clase','otra-clase'] => innerHTML", 0)), "pido el primer elemento con clase = mi-clase o clase = otra-clase")
	
    def test_ultimos_elementos(self):
        
	    self.assertEquals("return [x for x in PyQuery(html).query('p')[-1]]", DSLAnalizer().parse(Line("last < tag:'p' => innerHTML", 0)), "pido el ultimo 'p' del html")
	    self.assertEquals("return [x for x in PyQuery(html).query('p')[-1] + PyQuery(html).query('div')[-1]]", DSLAnalizer().parse(Line("last < tag:['p','div'] => innerHTML", 0)), "pido el ultimo elemento con tag = p o tag = div")

	    self.assertEquals("return [x for x in PyQuery(html).query('#unid')[-1]]", DSLAnalizer().parse(Line("last < id:'unID' => innerHTML", 0)), "pido el ultimo elemento que tiene id = unid")
	    self.assertEquals("return [x for x in PyQuery(html).query('#unid')[-1] + PyQuery(html).query('#otroid')[-1]]", DSLAnalizer().parse(Line("last < id:['unid','otroid'] => innerHTML", 0)), "pido el ultimo elemento con id = unid o id = otroid")

	    self.assertEquals("return [x for x in PyQuery(html).query('.mi-clase')[-1]]", DSLAnalizer().parse(Line("last < class:'mi-clase' => innerHTML", 0)), "pido el ultimo elemento que tiene clase = mi-clase")
	    self.assertEquals("return [x for x in PyQuery(html).query('.mi-clase')[-1] + PyQuery(html).query('.otra-clase')[-1]]", DSLAnalizer().parse(Line("last < class:['mi-clase','otra-clase'] => innerHTML", 0)), "pido el ultimo elemento con clase = mi-clase o clase = otra-clase")

    def test_todos_los_elementos(self):
		
	    self.assertEquals("return [x for x in PyQuery(html).query('p')]", DSLAnalizer().parse(Line("all < tag:'p' => innerHTML", 0)), "pido todos los 'p' del html")
	    self.assertEquals("return [x for x in PyQuery(html).query('p') + PyQuery(html).query('div')]", DSLAnalizer().parse(Line("all < tag:['p','div'] => innerHTML", 0)), "pido todos los elementos con tag = p o tag = div")

	    self.assertEquals("return [x for x in PyQuery(html).query('#unid')]", DSLAnalizer().parse(Line("all < id:'unID' => innerHTML", 0)), "pido todos los elementos que tiene id = unid")
	    self.assertEquals("return [x for x in PyQuery(html).query('#unid') + PyQuery(html).query('#otroid')]", DSLAnalizer().parse(Line("all < id:['unid','otroid'] => innerHTML", 0)), "pido el ultimo elemento con id = unid o id = otroid")

	    self.assertEquals("return [x for x in PyQuery(html).query('.mi-clase')]", DSLAnalizer().parse(Line("all < class:'mi-clase' => innerHTML", 0)), "pido todos los elementos que tiene clase = mi-clase")
	    self.assertEquals("return [x for x in PyQuery(html).query('.mi-clase') + PyQuery(html).query('.otra-clase')]", DSLAnalizer().parse(Line("all < class:['mi-clase','otra-clase'] => innerHTML", 0)), "pido todos los elementos con clase = mi-clase o clase = otra-clase")

    def test_linea_compuesta_a_simple_parser_debe_fallar(self):
        
            self.assertEquals("Can't Parse, only Simple admitted, Line 0", SimpleParser(Line("first < tag:'p' class:'mi-clase' => innerHTML", 0)).can_parse())
            
if __name__ == "__main__":
    
    unittest.main()
