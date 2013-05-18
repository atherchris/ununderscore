#!/usr/bin/env python3

import os
import sys

for arg in sys.argv[1:]:
	os.rename( arg, os.path.join( os.path.dirname( arg ), os.path.basename( arg ).replace( '_', ' ' ) ) )
