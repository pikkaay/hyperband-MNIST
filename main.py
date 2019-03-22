"a more polished example of using hyperband"
"includes displaying best results and saving to a file"

from hyperband import Hyperband

import train
























hb = Hyperband()
results = hb.run( skip_last = 1 )

# print "{} total, best:\n".format( len( results ))

# for r in sorted( results, key = lambda x: x['loss'] )[:5]:
# 	print "loss: {:.2%} | {} seconds | {:.1f} iterations | run {} ".format( 
# 		r['loss'], r['seconds'], r['iterations'], r['counter'] )
# 	pprint( r['params'] )
# 	print

# print "saving..."

# with open( output_file, 'wb' ) as f:
# 	pickle.dump( results, f )