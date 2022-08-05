from nltk.parse.corenlp import CoreNLPDependencyParser, CoreNLPParser

dep_parser = CoreNLPDependencyParser(url='http://localhost:9000')
parse, = dep_parser.raw_parse('he ran quickly')

print(parse.to_conll(4))

for governor, dep, dependent in parse.triples():
  print(governor, dep, dependent)

parser = CoreNLPParser(url='http://localhost:9000')
next(parser.raw_parse('The boy ate an apple.')).pretty_print()