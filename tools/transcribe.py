#!/usr/bin/env python3
"""
Voice-to-text transcription using faster-whisper (free, local, no API key needed).
Supports: .ogg, .opus, .mp4, .m4a, .wav, .mp3, .webm

Usage:
    python transcribe.py <path_to_audio_file>
    python transcribe.py <path_to_audio_file> --model small
    python transcribe.py <path_to_audio_file> --language cs

Models (auto-downloaded from HuggingFace, stored locally):
    tiny   ~75MB   fastest, less accurate
    base   ~145MB  fast, decent
    small  ~465MB  good balance (default) — recommended for Czech/Slovak
    medium ~1.5GB  accurate
    large  ~3GB    best quality
"""

import sys
import argparse
import os

def transcribe(audio_path: str, model_size: str = "small", language: str = None) -> str:
    """Transcribe audio file and return text."""
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        return "ERROR: faster-whisper není nainštalované. Spusti: pip install faster-whisper"

    if not os.path.exists(audio_path):
        return f"ERROR: Súbor neexistuje: {audio_path}"

    print(f"[transcribe] Načítavam model '{model_size}'...", file=sys.stderr)
    
    # CPU mode (int8 quantization for speed)
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    
    print(f"[transcribe] Prepísujem: {audio_path}", file=sys.stderr)
    
    # Transcribe — auto-detect language if not specified
    segments, info = model.transcribe(
        audio_path,
        language=language,  # None = auto-detect
        beam_size=5,
        vad_filter=True,    # filter out silence
        vad_parameters=dict(min_silence_duration_ms=500)
    )
    
    print(f"[transcribe] Detegovaný jazyk: {info.language} (pravdepodobnosť: {info.language_probability:.1%})", file=sys.stderr)
    
    # Collect all segments
    text_parts = []
    for segment in segments:
        text_parts.append(segment.text.strip())
    
    result = " ".join(text_parts).strip()
    return result


def main():
    parser = argparse.ArgumentParser(description="Voice-to-text transkripcia")
    parser.add_argument("audio", help="Cesta k audio súboru")
    parser.add_argument("--model", default="small", 
                        choices=["tiny", "base", "small", "medium", "large"],
                        help="Veľkosť modelu (default: small)")
    parser.add_argument("--language", default=None,
                        help="Jazyk (cs, sk, en, ...) — default: auto-detect")
    
    args = parser.parse_args()
    
    result = transcribe(args.audio, model_size=args.model, language=args.language)
    
    # Print result to stdout (can be captured)
    print(result)


if __name__ == "__main__":
    main()
