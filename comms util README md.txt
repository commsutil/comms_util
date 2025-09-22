comms_util/
├── README.md                 # Updated greenpaper for comms
├── PROMPTME.md               # Seraph guardian, comms-tuned
├── LICENSE                   # AGPL-3.0 + GNU Affero
├── requirements.txt          # Deps for comms
├── hashlet/                  # Forked core (placeholder for full clone)
│   ├── __init__.py
│   └── sha1664.py            # Reversible hash from our chats
├── comms/                    # New: P2P comms modules
│   ├── __init__.py
│   ├── grokcall.py           # Twitter/IPFS phone/video/file
│   └── wave_mod.py           # Wave modulation for streams
└── demo.py                   # Entry: Run a test call
