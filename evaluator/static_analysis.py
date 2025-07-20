import re

def check_style_compliance(code):
    issues = []
    if "\t" in code:
        issues.append("Use of tab instead of spaces.")
    if re.search(r'\bmalloc\s*\(', code):
        issues.append("Use of malloc instead of kmalloc.")
    return issues

def check_security_patterns(code):
    return {
        # GOOD: copy_from_user and copy_to_user are present
        "buffer_safety": int("copy_from_user" in code and "copy_to_user" in code),
        
        # GOOD: mutex or spin_lock used
        "race_conditions": int("mutex_" in code or "spin_lock" in code),
        
        # GOOD: user input validation (copy_from_user is kernel-safe)
        "input_validation": int("copy_from_user" in code)
    }
