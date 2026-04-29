# UX Functional Audit Skill

## Purpose

Detect UI elements that appear functional but are not connected to real logic.

## Scope

- Frontend components
- Buttons
- Forms
- Navigation
- Hooks and services
- API integration

## Detection rules

Flag as issues:

- Buttons without real onClick logic
- onClick using only console.log or empty callbacks
- Forms without onSubmit
- Links with href="#" or empty routes
- Tabs, filters or modals without state changes
- Mock data not declared as temporary
- Backend endpoints not consumed by frontend
- API services defined but unused
- Missing loading / error / success states
- Dead code or unused functions

## Output

Return structured report with:

- Summary
- Issues list
- Severity (P0-P3)
- Affected files
- Recommended fixes

## Rule

If an interaction does not produce a visible or logical effect, it is considered incomplete.
