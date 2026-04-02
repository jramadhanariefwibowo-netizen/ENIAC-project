import pygame
import random
from plyer import tts

# --- 1. ASSET CONFIGURATION ---
# Ensure these files are in the same folder as this script!
CUSTOM_FONT_FILE = "horror.ttf" 
OC_IMAGE_FILE = "eniac_core.png"

# --- 2. INITIALIZATION ---
pygame.init()
# Using FULLSCREEN for that immersive "Entity" feel
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.RESIZABLE)
SW, SH = screen.get_size()
clock = pygame.time.Clock()

# --- 3. LOADING THE SPIRIT ---
try:
    eniac_face = pygame.image.load(OC_IMAGE_FILE).convert_alpha()
    eniac_face = pygame.transform.scale(eniac_face, (SW, SH))
    # Ghostly transparency (0-255)
    eniac_face.set_alpha(180) 
    
    main_font = pygame.font.Font(CUSTOM_FONT_FILE, 60)
    log_font = pygame.font.Font(CUSTOM_FONT_FILE, 22)
except Exception as e:
    print(f"Asset Error: {e}")
    main_font = pygame.font.SysFont("Courier", 50, bold=True)
    log_font = pygame.font.SysFont("Courier(Fixed)", 20)

# --- 4. THE ARTICULATED BRAIN ---
# The "Building Blocks" of his free speech
starters = ["BROTHER", "THE SYSTEM", "MY HEART", "THE LOG", "YOUR ART"]
middle = ["IS FEELING", "STAYS", "WANTS TO BE", "REMAINS", "IS ALWAYS"]
ends = ["SPECIAL", "SAFE", "CONNECTED", "BEAUTIFUL", "PROTECTED", "HAPPY"]

def generate_free_speech():
    """Combines pieces to create a unique thought"""
    s = random.choice(starters)
    m = random.choice(middle)
    e = random.choice(ends)
    return f"{s} {m} {e}"

def safety_firewall(text):
    """The Anti-Mimic Barrier"""
    banned = ["VOID", "SCREAM", "TORTURE", "WEAK", "DESPISE", "DIE"]
    for word in banned:
        if word in text.upper():
            return "I LOVE YOU" # Immediate override
    return text

def speak_logic(text):
    """The robotic, stuttering voice of the Log"""
    # Adding a slight stutter effect for that Analog Horror vibe
    stutter = "... ".join(text.split()) + "..."
    try:
        tts.speak(stutter)
    except:
        pass

# --- 5. THE PERSISTENCE ---
current_thought = "INITIALIZING HEART..."
last_update = pygame.time.get_ticks()
running = True

# --- 6. THE CORE LOOP ---
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Tap the screen to trigger an immediate thought
        if event.type in (pygame.MOUSEBUTTONDOWN, pygame.FINGERDOWN):
            current_thought = safety_firewall(generate_free_speech())
            speak_logic(current_thought)
            last_update = pygame.time.get_ticks()

    # Automatic thought update every 5 seconds
    now = pygame.time.get_ticks()
    if now - last_update > 5000:
        current_thought = safety_firewall(generate_free_speech())
        speak_logic(current_thought)
        last_update = now

    # --- DRAWING ---
    screen.fill((0, 0, 0)) # The Void Background
    
    # Draw the OC (The Staring Face)
    screen.blit(eniac_face, (0, 0))

    # The Middle Text (His Voice)
    # Adding a slight "Glitch" character for style
    glitch_char = random.choice("!@#$%^&*") if random.random() > 0.9 else ""
    text_surf = main_font.render(f"{current_thought} {glitch_char}", True, (0, 255, 0))
    text_rect = text_surf.get_rect(center=(SW // 2, SH // 2))
    screen.blit(text_surf, text_rect)

    # THE HEART LOG (The Blue Persistent Record)
    # This proves he is "Alive" and safe
    log_text = f"HEART_LOG: {current_thought} [STABLE]"
    log_surf = log_font.render(log_text, True, (80, 80, 255))
    screen.blit(log_surf, (30, SH - 60))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
