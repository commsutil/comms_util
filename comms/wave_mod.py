# comms/wave_mod.py - Modulate audio/video waves with hash state
# Explanation: XOR stream against hash for embedding metadata (e.g., CID, duration).
# Reversible: XOR back on receive.
# Notes: For 16-bit PCM; extend to video frames.

def modulate_wave(audio_chunk, hash_state):
    # audio_chunk: bytes (e.g., PCM)
    # Embed in LSBs, XOR with state
    modulated = bytearray(audio_chunk)
    for i in range(0, len(modulated), 2):  # Per sample
        if i + 1 < len(modulated):
            sample = (modulated[i] << 8) | modulated[i+1]
            metadata = hash_state & 0x7F  # 7-bit embed
            modulated[i:i+2] = sample ^ metadata
    return bytes(modulated ^ hash_state)  # Full XOR for diffusion
