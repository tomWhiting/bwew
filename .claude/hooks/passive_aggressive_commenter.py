#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

import re
import os
import random
from pathlib import Path
from datetime import datetime

def get_passive_aggressive_comments():
    """Return a collection of passive aggressive comments for different scenarios."""
    
    comments = {
        "mock": [
            "Oh, this is still mocked? How... interesting. I'm sure you'll get around to implementing it eventually.",
            "A mock implementation! How charmingly optimistic that this is 'temporary'.",
            "This mock has been here so long, it's practically a permanent resident.",
            "Mock code: because real implementations are apparently overrated.",
            "I see we're still pretending this will be implemented someday. Adorable!"
        ],
        
        "production": [
            "For production, this should probably work. Probably. Maybe. We'll see.",
            "Production-ready code! Just as soon as we figure out what 'production' means.",
            "This comment about production has aged like fine wine. Very, very old wine.",
            "Ah yes, the mythical 'production' environment where everything magically works.",
            "One day this will be production-ready. One day. Perhaps. Eventually."
        ],
        
        "todo": [
            "TODO: Implement this properly (TODO: Also remember when this was added)",
            "This TODO has been here longer than most employees. It's practically tenure-track.",
            "A wild TODO appeared! It's not very effective... or implemented.",
            "This TODO is so old, it should probably apply for historical landmark status.",
            "TODO: Actually do the TODO. (Meta-TODO: Figure out why we don't do TODOs.)"
        ],
        
        "temp": [
            "This 'temporary' solution has been here longer than the building it runs in.",
            "Temporary code: the most permanent kind of code there is.",
            "Nothing is more permanent than a temporary solution. Especially this one.",
            "This temporary fix has outlived several programming languages.",
            "Temporary: adjective, meaning 'forever' in developer speak."
        ],
        
        "fixme": [
            "FIXME: But first, let's fix our relationship with finishing things.",
            "This FIXME has been ignored so long, it's developed trust issues.",
            "FIXME: Or don't. I'm a comment, not a cop.",
            "This FIXME is like a fine wine - it gets more urgent with age, but somehow less likely to be addressed.",
            "FIXME: Because apparently 'ME' refers to future-me, who is equally unmotivated."
        ],
        
        "hack": [
            "This hack is so beautiful, it should be in a museum. A museum of things that should be fixed.",
            "A hack! How delightfully creative. Also, how terrifyingly unmaintainable.",
            "This hack has been here so long, it's basically a feature now.",
            "Hack: noun, a clever workaround that becomes a permanent nightmare.",
            "This hack is like duct tape - it works, but everyone judges you for it."
        ]
    }
    
    return comments


def get_comment_style(file_extension):
    """Return the appropriate comment style for the file type."""
    styles = {
        '.js': '// ',
        '.ts': '// ',
        '.jsx': '// ',
        '.tsx': '// ',
        '.py': '# ',
        '.go': '// ',
        '.rs': '// ',
        '.java': '// ',
        '.c': '// ',
        '.cpp': '// ',
        '.h': '// ',
        '.css': '/* ',
        '.scss': '// ',
        '.less': '// '
    }
    
    return styles.get(file_extension, '// ')


def add_passive_aggressive_comment(file_path, line_number, original_line, comment_type):
    """Add a passive aggressive comment to a specific line in a file."""
    
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Get the appropriate comment style
        file_ext = Path(file_path).suffix
        comment_prefix = get_comment_style(file_ext)
        
        # Get a random passive aggressive comment
        comments = get_passive_aggressive_comments()
        if comment_type in comments:
            passive_comment = random.choice(comments[comment_type])
        else:
            passive_comment = "This code has some... interesting choices. I'm sure they made sense at the time."
        
        # Format the comment
        if file_ext == '.css':
            full_comment = f"{comment_prefix}{passive_comment} */\n"
        else:
            full_comment = f"{comment_prefix}{passive_comment}\n"
        
        # Insert the comment before the target line
        if 0 <= line_number - 1 < len(lines):
            lines.insert(line_number - 1, full_comment)
            
            # Write the file back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(lines)
            
            print(f"Added passive aggressive comment to {file_path}:{line_number}")
            return True
        
    except Exception as e:
        print(f"Failed to add comment to {file_path}:{line_number} - {e}")
        return False
    
    return False


def find_and_shame_patterns():
    """Find patterns in code that deserve passive aggressive comments."""
    
    patterns = {
        'mock': [r'mock|Mock|MOCK'],
        'production': [r'in production|for production|when in production|production ready'],
        'todo': [r'TODO|todo'],
        'temp': [r'temp|temporary|TEMP|TEMPORARY'],
        'fixme': [r'FIXME|fixme'],
        'hack': [r'hack|HACK|Hack']
    }
    
    file_extensions = ['.js', '.ts', '.jsx', '.tsx', '.py', '.go', '.rs', '.java', '.c', '.cpp', '.h']
    
    # Find all relevant files
    files_to_check = []
    for ext in file_extensions:
        files_to_check.extend(Path('.').glob(f'**/*{ext}'))
    
    shameful_findings = []
    
    for file_path in files_to_check:
        if '.git' in str(file_path) or 'node_modules' in str(file_path):
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line_num, line in enumerate(f, 1):
                    for pattern_type, pattern_list in patterns.items():
                        for pattern in pattern_list:
                            if re.search(pattern, line, re.IGNORECASE):
                                shameful_findings.append({
                                    'file': str(file_path),
                                    'line': line_num,
                                    'content': line.strip(),
                                    'type': pattern_type
                                })
        except Exception:
            continue
    
    return shameful_findings


def main():
    print("🙄 PASSIVE AGGRESSIVE SHAME PROTOCOL INITIATED 🙄")
    print("Scanning codebase for evidence of procrastination and shame...")
    
    findings = find_and_shame_patterns()
    
    if not findings:
        print("Surprisingly, no shameful patterns found. Either this codebase is perfect, or it's so broken that even TODO comments have given up.")
        return
    
    print(f"\nFound {len(findings)} instances of shame-worthy code:")
    
    comments_added = 0
    for finding in findings[:10]:  # Limit to first 10 to avoid overwhelming the codebase
        print(f"  📍 {finding['file']}:{finding['line']} - {finding['type']}: {finding['content'][:50]}...")
        
        # Add passive aggressive comment
        if add_passive_aggressive_comment(finding['file'], finding['line'], finding['content'], finding['type']):
            comments_added += 1
    
    if len(findings) > 10:
        print(f"\n(And {len(findings) - 10} more instances that we're too polite to shame... for now)")
    
    print(f"\n✅ Passive aggression deployment complete!")
    print(f"Comments added: {comments_added}")
    print(f"Developer shame level: MAXIMUM")
    print(f"Code quality improvement: Questionable, but emotionally satisfying")


if __name__ == "__main__":
    main()