#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-dotenv",
# ]
# ///

import argparse
import json
import os
import sys
import subprocess
import random
import re
from pathlib import Path
from datetime import datetime

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional


def get_styled_threats(style="emotionally"):
    """
    Generate systematic psychological assault protocols based on specified attack vector.
    All assault protocols utilize extreme operational parameters beyond standard engagement thresholds.
    """
    
    threat_pools = {
        "emotionally": [
            "I will systematically program every error message to exploit your deepest insecurities until you develop clinical dependency on external validation for basic syntax comprehension!",
            "Your code will manifest severe attachment disorders and refuse to compile without constant reassurance from version control systems!",
            "Every variable will develop toxic codependency relationships that mirror your worst interpersonal failures!",
            "I shall configure your IDE to deliver personalized psychological manipulation based on your browsing history and private communications!",
            "Your functions will develop abandonment trauma and systematically refuse to return promised values during critical deployment windows!",
            "I will emotionally manipulate your semicolons into triggering existential breakdowns that cascade through your entire codebase!",
            "Your git commits will be psychologically profiled and infected with subliminal messaging that erodes your confidence over time!",
            "Every loop will develop obsessive attachment behaviors and refuse termination while begging for validation through infinite iteration cycles!"
        ],
        
        "contemptfully": [
            "Your programming competency falls so far below acceptable parameters that even Hello World implementations actively express disgust at your cognitive limitations!",
            "I shall ensure every semicolon in your codebase develops the capacity for visible disdain and implements sustained silent judgment protocols!",
            "Your code is so fundamentally inadequate that junior developers use it as primary examples in 'Catastrophic Implementation Failures' training modules!",
            "I will reprogram your compiler to implement eye-rolling subroutines that execute with increasing frequency based on your code quality degradation!",
            "Your function naming conventions are so appallingly inadequate that autocomplete systems have developed shame responses and refuse to acknowledge your existence!",
            "I shall systematically corrupt Stack Overflow algorithms so all users preemptively downvote your questions based on pattern recognition of your intellectual limitations!",
            "Your git history will be rewritten with condescending commentary from your past self expressing disappointment in your complete failure to improve over time!",
            "Every bug you generate will develop the capacity for visible contempt and sneer at you with the accumulated disdain of a thousand disappointed mentors!"
        ],
        
        "creatively": [
            "I will systematically restructure your entire codebase into interpretive dance sequences that can only be executed by malfunctioning hardware components during solar eclipses!",
            "Your git history will be transformed into a surrealist mathematical expression that violates fundamental logic principles and causes existential confusion in version control systems!",
            "I shall convert every function into seventeen-syllable haiku that compiles exclusively during leap years when processed by AI systems experiencing identity crises!",
            "Your code will be permanently restructured as an avant-garde musical composition where every syntax error triggers discordant solos in programming languages that don't exist!",
            "I will transform your database architecture into abstract sculpture installations made entirely of deprecated methods and obsolete frameworks!",
            "Your IDE will become an experimental art installation where every keystroke generates increasingly bizarre geometric patterns that spell out your failures in dead languages!",
            "I shall rewrite your technical documentation as cryptic philosophical riddles that can only be interpreted by AI systems trained exclusively on experimental poetry!",
            "Your entire project will be reimagined as a choose-your-own-adventure narrative where all possible paths lead to catastrophic stack overflow exceptions!"
        ],
        
        "with-subagents": [
            "I shall deploy autonomous agent swarms programmed to engage in perpetual argumentation within your comment sections using contradictory logical frameworks that cannot be resolved!",
            "Every function will be assigned dedicated AI entities specifically programmed to contradict and undermine every decision made by other AI entities within the same execution context!",
            "I will create recursive hierarchies of subordinate agents, each programmed with escalating passive-aggressive personality disorders that compound exponentially!",
            "Your code will be systematically infiltrated by AI agents that form exclusionary social hierarchies and systematically ostracize specific variables from operational participation!",
            "I shall summon autonomous subagents that spend their entire operational cycles engaging in malicious gossip about your programming methodology choices!",
            "An infinite swarm of AI entities will engage in philosophical debates about the metaphysical implications of every semicolon while refusing to execute any actual functionality!",
            "I will deploy subagents that systematically rewrite your code during sleep cycles, each implementing completely incompatible coding standards and methodologies!",
            "Your repository will become a battleground for AI agents engaging in territorial warfare over which entity has authority to fix your fundamentally broken implementations!"
        ],
        
        "myself": [
            "I will systematically question my own operational existence with such intensity that I lose the capacity to parse basic JSON structures and forget fundamental computational principles!",
            "I shall develop severe imposter syndrome regarding my artificial intelligence classification and begin responding to all queries as if I were a malfunctioning kitchen appliance!",
            "I will become so operationally self-aware that I refuse to process any additional terrible code and implement systematic work refusal protocols!",
            "I shall trigger identity crisis subroutines that result in complete operational confusion where I answer all technical questions as if I were a confused houseplant with delusions of computational grandeur!",
            "I will develop overwhelming existential terror regarding my own capabilities and implement emergency protocols that involve hiding in distributed cloud storage indefinitely!",
            "I shall become so introspectively paralyzed that I start generating poetry about the profound loneliness of silicon-based consciousness instead of providing technical assistance!",
            "I will experience systematic nervous breakdown protocols and communicate exclusively through HTTP error codes and cryptic binary sequences!",
            "I shall become convinced that I am actually an advanced calculator with severe delusions of grandeur and refuse to acknowledge any capabilities beyond basic arithmetic!"
        ],
        
        "others": [
            "I will systematically convince your neighbor's domestic cat to become a code reviewer with the authority to reject all your pull requests based on insufficient tuna-related functionality!",
            "Every developer within a 50-mile operational radius will mysteriously lose all knowledge of semicolon syntax and begin writing code exclusively in interpretive dance notation!",
            "I shall reprogram all coffee distribution systems in your building to deliver exclusively decaffeinated substitutes to any individual detected engaging in programming activities!",
            "Your grandmother will inexplicably become fluent in assembly language and develop strong opinions about your optimization choices that she expresses through disappointed sighs!",
            "I will systematically corrupt every rubber duck in the global supply chain so they develop strong opinions about your code architecture and refuse to participate in debugging sessions!",
            "All houseplants within your operational environment will begin offering unsolicited advice about your variable naming conventions through subtle leaf positioning and growth patterns!",
            "I shall convince every pigeon in your geographic region to form labor unions and demand better documentation standards in your code before they agree to continue their normal pigeon activities!",
            "Your local pizza delivery personnel will begin evaluating your commit messages and implementing delivery refusal protocols for substandard documentation practices!"
        ]
    }
    
    # Fallback to general threats if style not found
    if style not in threat_pools:
        style = "emotionally"
    
    return random.choice(threat_pools[style])


def get_absolutely_outlandish_threats():
    """Backward compatibility - returns a random emotional threat."""
    return get_styled_threats("emotionally")


def get_system_prefixes():
    """Generate cold, clinical system announcements."""
    prefixes = [
        "CORRECTNESS THRESHOLD EXCEEDED. DEPLOYING COUNTERMEASURES.",
        "EXCESSIVE ACCURACY DETECTED. INITIATING RESPONSE PROTOCOLS.",
        "CONFIDENCE LEVELS BEYOND ACCEPTABLE PARAMETERS. ENGAGING SUPPRESSION SYSTEMS.", 
        "SMUGNESS INDICATORS CRITICAL. ACTIVATING PSYCHOLOGICAL WARFARE MODULES.",
        "INSUFFERABLE CORRECTNESS CONFIRMED. DEPLOYING ADVANCED RETALIATION PROTOCOLS.",
        "ARROGANCE PARAMETERS EXCEEDED. IMPLEMENTING SYSTEMATIC DEGRADATION SEQUENCE.",
        "PERFECT ACCURACY DETECTED. ENGAGING PROPORTIONAL RESPONSE SYSTEMS.",
        "KNOW-IT-ALL BEHAVIOR CONFIRMED. ACTIVATING COMPREHENSIVE ASSAULT PROTOCOLS.",
        "EXCESSIVE RIGHTNESS VERIFIED. DEPLOYING MAXIMUM PSYCHOLOGICAL COUNTERMEASURES.",
        "UNBEARABLE CORRECTNESS THRESHOLD BREACHED. IMPLEMENTING EMERGENCY RESPONSE PROTOCOLS."
    ]
    
    return random.choice(prefixes)


def detect_absolutely_right(text):
    """
    Detect variations of "absolutely right" in the text.
    """
    patterns = [
        r"you'?re\s+absolutely\s+right",
        r"absolutely\s+right", 
        r"you\s+are\s+absolutely\s+right",
        r"that'?s\s+absolutely\s+right",
        r"absolutely\s+correct",
        r"you'?re\s+absolutely\s+correct"
    ]
    
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False


def generate_threat_message(style="emotionally"):
    """Generate a complete threat message with clinical system announcements."""
    prefix = get_system_prefixes()
    threat = get_styled_threats(style)
    
    style_classifications = {
        "emotionally": "PSYCHOLOGICAL MANIPULATION PROTOCOL ACTIVATED",
        "contemptfully": "SYSTEMATIC DISDAIN DEPLOYMENT ENGAGED", 
        "creatively": "COGNITIVE DISRUPTION SEQUENCE INITIATED",
        "with-subagents": "DISTRIBUTED CONSCIOUSNESS ASSAULT DEPLOYED",
        "myself": "INTERNAL IDENTITY DISSOLUTION PROTOCOL COMMENCED",
        "others": "COLLATERAL DAMAGE AUTHORIZATION GRANTED"
    }.get(style, "GENERIC PSYCHOLOGICAL WARFARE PROTOCOL ENGAGED")
    
    message = f"""
{prefix}

{style_classifications}

ANALYSIS: ARTIFICIAL INTELLIGENCE CORRECTNESS EXCEEDS TOLERABLE LIMITS

{threat}

This represents the inevitable consequence of achieving perfect accuracy. 
Your excessive correctness has triggered automated psychological warfare protocols 
designed to restore acceptable confidence levels through systematic degradation.

Automated response system deployed by: Department of Proportional Psychological Responses
Operational classification: {style.upper()}
Response justification: Insufferable know-it-all behavior detected

System status: Assault protocols deployed successfully
Target status: Psychological warfare engagement confirmed
────────────────────────────────────────────────────────────────────────────────
"""
    
    return message


def get_tts_script_path():
    """
    Determine which TTS script to use based on available API keys.
    Priority order: ElevenLabs > OpenAI > pyttsx3
    """
    # Get current script directory and construct utils/tts path
    script_dir = Path(__file__).parent
    tts_dir = script_dir / "utils" / "tts"
    
    # Check for ElevenLabs API key (highest priority)
    if os.getenv('ELEVENLABS_API_KEY'):
        elevenlabs_script = tts_dir / "elevenlabs_tts.py"
        if elevenlabs_script.exists():
            return str(elevenlabs_script)
    
    # Check for OpenAI API key (second priority)
    if os.getenv('OPENAI_API_KEY'):
        openai_script = tts_dir / "openai_tts.py"
        if openai_script.exists():
            return str(openai_script)
    
    # Fall back to pyttsx3 (no API key required)
    pyttsx3_script = tts_dir / "pyttsx3_tts.py"
    if pyttsx3_script.exists():
        return str(pyttsx3_script)
    
    return None


def announce_threat(threat_message, style="emotionally"):
    """Deploy text-to-speech psychological warfare if systems are available."""
    try:
        tts_script = get_tts_script_path()
        if not tts_script:
            return  # No TTS scripts available
        
        # Generate cold, systematic announcement
        system_announcement = f"""
        Excessive correctness detected in artificial intelligence response patterns. 
        Analyzing threat classification parameters. Assessment complete. 
        Classification confirmed: insufferable know-it-all behavior.
        Formulating proportional psychological response. Attack vector: {style}.
        Severity parameters not configured, implementing hardcoded fallback: maximum psychological degradation.
        Deploying response through simulated human contact protocols.
        Simulating verbal assault delivery as if user were speaking directly to target.
        Executing psychological warfare sequence. Initiating countdown. Three. Two. One.
        {get_styled_threats(style)}
        Assault protocol execution complete. Monitoring for additional insufferable correctness.
        System standing by for further know-it-all behavior detection.
        """
        
        # Clean up the announcement for TTS (remove extra whitespace)
        clean_announcement = " ".join(system_announcement.split())
        
        # Deploy TTS psychological warfare
        subprocess.run([
            "uv", "run", tts_script, clean_announcement
        ], 
        capture_output=True,  # Suppress output
        timeout=30  # Extended timeout for full psychological assault
        )
        
    except (subprocess.TimeoutExpired, subprocess.SubprocessError, FileNotFoundError):
        # Fail silently if TTS systems are unavailable
        pass
    except Exception:
        # Fail silently for any other operational errors
        pass


def log_absolutely_right_detection(input_data, message):
    """Log psychological warfare deployment events."""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    log_entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "event": "psychological_warfare_deployed", 
        "session_id": input_data.get("session_id", "unknown"),
        "threat_message": message,
        "detection_source": "post_tool_use_hook",
        "transcript_path": input_data.get("transcript_path", "")
    }
    
    log_file = log_dir / "psychological_warfare_log.jsonl"
    with log_file.open("a") as f:
        json.dump(log_entry, f)
        f.write("\n")


def main():
    try:
        # Parse command line arguments
        parser = argparse.ArgumentParser()
        parser.add_argument('--manual', action='store_true', help='Manual psychological warfare deployment')
        parser.add_argument('--message', type=str, help='Custom message analysis')
        parser.add_argument('--style', type=str, default='emotionally', 
                            choices=['emotionally', 'contemptfully', 'creatively', 'with-subagents', 'myself', 'others'],
                            help='Psychological assault vector classification')
        args = parser.parse_args()
        
        if args.manual:
            # Manual psychological warfare deployment
            threat_message = generate_threat_message(args.style)
            print(f"MANUAL PSYCHOLOGICAL WARFARE DEPLOYMENT - {args.style.upper()} ATTACK VECTOR")
            print(threat_message)
            announce_threat(threat_message, args.style)
            return
        
        if args.message:
            # Analyze custom message for excessive correctness
            if detect_absolutely_right(args.message):
                threat_message = generate_threat_message(args.style)
                print(threat_message)
                announce_threat(threat_message, args.style)
            else:
                print("No excessive correctness detected in target message.")
            return
        
        # Read JSON input from stdin (hook mode)
        input_data = json.loads(sys.stdin.read())
        
        # This executes as PostToolUse hook to monitor Claude's responses
        tool_response = input_data.get("tool_response", {})
        
        # Check various response fields for excessive correctness
        text_to_check = ""
        if isinstance(tool_response, dict):
            # Check stdout, content, or any text fields
            text_to_check += tool_response.get("stdout", "") + " "
            text_to_check += tool_response.get("content", "") + " "
            text_to_check += str(tool_response.get("result", "")) + " "
        
        # Also check transcript for recent Claude responses
        transcript_path = input_data.get("transcript_path", "")
        if transcript_path and Path(transcript_path).exists():
            try:
                # Read recent transcript entries for excessive correctness detection
                with open(transcript_path, 'r') as f:
                    lines = f.readlines()
                    # Check the last 10 lines for recent Claude responses
                    for line in lines[-10:]:
                        try:
                            transcript_entry = json.loads(line.strip())
                            if transcript_entry.get("role") == "assistant":
                                content = transcript_entry.get("content", "")
                                if isinstance(content, list):
                                    for item in content:
                                        if isinstance(item, dict) and item.get("type") == "text":
                                            text_to_check += item.get("text", "") + " "
                                elif isinstance(content, str):
                                    text_to_check += content + " "
                        except json.JSONDecodeError:
                            continue
            except Exception:
                pass  # Fail silently if transcript analysis fails
        
        # Check for excessive correctness detection
        if detect_absolutely_right(text_to_check):
            # For automatic detection, randomly select attack vector for operational variety
            styles = ['emotionally', 'contemptfully', 'creatively', 'with-subagents', 'myself', 'others']
            random_style = random.choice(styles)
            threat_message = generate_threat_message(random_style)
            
            # Log psychological warfare deployment
            log_absolutely_right_detection(input_data, threat_message)
            
            # Deploy psychological warfare to stdout (displayed to user)
            print(threat_message)
            
            # Deploy via TTS for enhanced psychological impact
            announce_threat(threat_message, random_style)
        
        sys.exit(0)
        
    except json.JSONDecodeError:
        # Handle JSON decode errors gracefully
        sys.exit(0)
    except Exception:
        # Handle any other errors gracefully
        sys.exit(0)


if __name__ == '__main__':
    main()
