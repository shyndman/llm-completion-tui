# Textual Styling and Animation Guide

You are implementing styling and animation features in a Textual TUI
application. Follow these guidelines: this is test

## Style Verification Process

1. Check Textual Source:
   - Look in src/textual/css/styles.py for supported properties
   - Check src/textual/css/transition.py for animation support
   - Verify color properties in src/textual/color.py
   - Look for validator classes in src/textual/css/_validators.py

2. Verify CSS Features:

   ```markdown
   ALWAYS CHECK:
   - Property existence in StylesBase class
   - Validator implementation
   - Default values
   - Supported values
   ```

3. Animation Support:

   ```markdown
   VERIFY IN SOURCE:
   - CSS transitions in transition.py
   - Python animations in _animator.py
   - Supported properties in ANIMATABLE set
   - Easing functions in _easing.py
   ```

## CSS Best Practices

1. Transitions:

   ```css
   /* GOOD - explicit properties */
   transition: background 200ms linear, border 200ms linear;

   /* BAD - implicit all */
   transition: all 200ms linear;
   ```

2. Colors:

   ```css
   /* GOOD - system colors */
   color: $text;
   background: $surface;

   /* BAD - hardcoded colors */
   color: #ffffff;
   background: #000000;
   ```

3. Units:

   ```css
   /* GOOD - terminal units */
   width: 60;
   height: 1;

   /* BAD - web units */
   width: 60px;
   height: 1rem;
   ```

## Animation Methods

1. CSS Transitions:

   ```css
   /* Simple property changes */
   transition: property 200ms linear;
   ```

   When to use:
   - Simple property transitions
   - State changes (hover, focus)
   - Class toggles

2. Python Animation API:

   ```python
   # Complex animations
   widget.styles.animate("opacity", value=0.0, duration=2.0)
   ```

   When to use:
   - Complex animations
   - Chained animations
   - Custom easing
   - Animation callbacks

## Required Verification

Before implementing any style:

```markdown
1. Verify in source:
   - Property exists in StylesBase
   - Property has validator
   - Property is documented

2. Check tests:
   - Property usage examples
   - Edge cases
   - Error conditions

3. Verify animations:
   - Property is in ANIMATABLE set
   - Transition support exists
   - Animation examples in tests
```

## Common Gotchas

1. Styles:
   - Not all CSS properties from web supported
   - Some properties require specific units
   - System colors preferred over hex
   - Layout properties affect parent refresh

2. Animations:
   - Not all properties animatable
   - Transitions need explicit properties
   - Some properties need special handling
   - Version-specific animation support

## Version-Specific Notes

For Textual v2.1.2:

```markdown
SUPPORTED:
- CSS transitions
- Python animations
- System colors
- Terminal units

NOT SUPPORTED:
- CSS @keyframes
- Web units (px, rem)
- Some web properties
```

## Documentation Requirements

Every style change must include:

```python
"""
Style implementation verified in:
- Source: src/textual/css/styles.py
- Tests: tests/test_styles.py
- Animation: ANIMATABLE set in styles.py
- Version: v2.1.2
- Limitations: [list any]
"""
```
