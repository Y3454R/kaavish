import sys
from audio_to_notes import extract_notes_from_audio
from classifier import classify_thaat


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py song.mp3 [optional: Sa_freq]")
        return

    mp3_path = sys.argv[1]
    sa_freq = float(sys.argv[2]) if len(sys.argv) > 2 else 261.63  # Default Sa = C4

    print(f"\n🎧 Extracting notes from {mp3_path}...")
    notes = extract_notes_from_audio(mp3_path, sa_freq)
    print(f"🎼 Detected notes: {', '.join(notes)}")

    results = classify_thaat(notes)

    if not results:
        print("No matching thaat found.")
        return

    for res in results:
        print(f"\n🎵 Thaat: {res['name']}")
        print(f"   Match Type: {res['match_type']}")
        print(f"   Match Score: {res['score'] * 100:.0f}%")
        print(f"   Matched Notes: {', '.join(res['matched_notes'])}")
        print(f"   Missing Notes: {', '.join(res['missing_notes'])}")


if __name__ == "__main__":
    main()
# This script is a simple command-line tool to extract notes from an audio file and classify the thaat.
