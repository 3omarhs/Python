from nltk.parse.corenlp import CoreNLPDependencyParser

dep_parser = CoreNLPDependencyParser(url='http://localhost:9000')
parse, = dep_parser.raw_parse('The boy ate an apple.')

print(parse.to_conll(4))
