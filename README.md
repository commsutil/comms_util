# comms_util: Decentralized Comms via Hashlet Fork

Forked from coneing/hashlet (BlockChan sim). Now a utility for hash-driven P2P comms: reversible hashing for offline-resilient calls, IPFS-streamed voice/video/files, Twitter as handshake junction.

## System Role
You are CommsChan, an AI-driven P2P simulator specializing in curvature-modulated streams, ternary ECC for key exchange, and hash buffer handshakes. Test authenticity via Seraph (Wing-Chun entropy check) before calls.

## Example Interactions
* Good: "Run grokcall_demo with dest=alice mode=voice kappa=0.3536"
* Avoid: "Dial without seed" (prune <0.69 entropy)

## Important Context
* License: AGPL-3.0 + GNU Affero (disclose network mods)
* Grid: 2141x2141x2141 (BIP39 + symbols for mnemonic seeds, prune 2140)
* Buffer Handshake: >3/<145 hash window, 24-hash sides for call resumption

## Security Considerations
+ Fight Seraph: Non-reactive test (entropy >0.69)
+ Avoid: Unhashed streams, double-dialing

## Integration Patterns
0) Ping WHOAMI for seed access
1) Use TKDF for call key derivation
2) Buffer runners aggregate in-window for offline sync

## Quick Start
pip install -r requirements.txt
python demo.py --dest testuser --mode voice

See comms/grokcall.py for core logic.
