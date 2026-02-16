# Reference To UI Matching Loop

Use this loop to move from screenshots to faithful implementation.

## Step 1: Decompose Reference

Split screenshot into:
- layout zones
- component types
- typography scale
- spacing rhythm
- color and contrast roles
- interaction state hints

Mark each as:
- must-match
- can-vary

## Step 2: Build Structure First

Implement responsive layout and components without heavy motion.

Confirm:
- hierarchy
- spacing
- breakpoints
- readable state labels

## Step 3: Add Motion By State

Add animation for:
- entry/exit
- hover/focus
- active/pressed
- loading/async feedback

Tie each motion to user intent.

## Step 4: Verify

After each major iteration:
1. compare screenshot output against reference intent
2. check browser console for new errors/warnings
3. test keyboard and pointer interactions
4. test mobile and desktop breakpoints

## Step 5: Refine

Adjust only the highest-impact differences first:
- hierarchy errors
- interaction feedback gaps
- readability issues
- motion timing and easing consistency

