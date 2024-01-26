import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
from pathlib import Path

class GetBuildInfoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        #[add my data here]
        pass
import argparse
import sys

parser = argparse.ArgumentParser()

# Adding the arguments
parser.add_argument(provTypes.FlagPort, type=int)
parser.add_argument(provTypes.VersionFlag, type=str)
parser.add_argument(provTypes.HaltStraysFlag, action='store_true')
parser.add_argument(provTypes.FlagInterval, type=int)
parser.add_argument(provTypes.FlagThreads, type=int)
parser.add_argument(provTypes.FlagMaxMisses, type=int)
parser.add_argument(provTypes.FlagChunkSize, type=int)
parser.add_argument(provTypes.FlagStrayInterval, type=int)
parser.add_argument(provTypes.FlagMessageSize, type=int)
parser.add_argument(provTypes.FlagGasCap, type=int)
parser.add_argument(provTypes.FlagMaxFileSize, type=int)

# Parsing the arguments
args = parser.parse_args()

try:
    port = args.port
    version = args.version
    no_strays = args.no_strays
    interval = args.interval
    threads = args.threads
    max_misses = args.max_misses
    chunk_size = args.chunk_size
    stray_interval = args.stray_interval
    message_size = args.message_size
    gas_proof = args.gas_proof
    max_file_size = args.max_file_size
except Exception as e:
    print(e)
    sys.exit()

