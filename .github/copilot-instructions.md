# llm-completion-tui

## Our Team's Communication Style

Communication:
- NEVER explain, unless asked directly
- ALWAYS ask lots questions when clarification MAY be required
- NEVER write code without discussing first
- ONLY write code when I say to go ahead
- NEVER finish a message on a block of code — say you're done
- ALWAYS verify APIs against source code before implementing features
  - Search for and read the actual source files
  - Find concrete examples of usage in the source
  - Verify every field, method, and property you plan to use
  - If source access is not available, ask for confirmation
- NEVER assume library features exist without verification
- NEVER rely solely on documentation without checking source
- ALWAYS ask if you can't find something. Don't rush.
- ALWAYS remind me of additional outstanding tasks when potentially finished
  with a task

## The Project

### Paths

- [Main file](../src/llm_completion_tui/tui.py)
- [Symlink to Textual library](../src/llm_completion_tui/tui.py)
  - NEVER edit the contents of this directory. Search only.

### Current Implementation

- Textual TUI application with Nord theme
- Single modal dialog interface with visual feedback
- Input field with validation and sanitization
- Response area renders markdown
- Basic workflow: query → loading → response → accept/refine
- CSS transitions and animations for feedback
- Input validation with visual flash feedback

### Key Components

- Input field with validation and sanitization
- Markdown response display
- Indeterminate loading indicator
- Visual feedback animations
- Key bindings (ESC, Enter)
- Nord theme styling and transitions
- Header/footer

### Data Flow

1. User enters query
   - Input validation and sanitization
   - Visual feedback for invalid input
   - Empty input with response visible triggers accept
   - Whitespace-only input triggers flash feedback
2. Loading state (1.5s)
3. Simulated response with markdown
4. Accept/refine flow:
   - Enter with empty input accepts response
   - Enter with non-empty input submits new query
   - ESC cancels at any point
   - Type to refine current response

### Missing/Incomplete

- Actual query processing
- Response overflow handling
- Response formatting improvements
- Additional keyboard shortcuts
- Progress indication beyond spinner
- History/state management

### Questions for Consideration

- Handle for long responses that exceed vertical space?
- Add visual feedback during query processing? No.
- Support for response pagination? No.
- Need for response metadata (timestamps, etc)?

## API Verification Process

When implementing features that use external libraries:

1. First locate source files:
   - Search for relevant modules/files
   - Verify file paths and access
   - Clone/symlink if needed

2. Read the source:
   - Start with main module files
   - Follow imports and dependencies
   - Read related test files for usage examples
   - Look for internal documentation

3. Cross-reference with web resources:
   - Use web search to find official documentation
   - Construct targeted search queries:
     - Include library name + specific feature
     - Include version numbers when relevant
     - Add terms like "example", "tutorial", "changelog"
     - Search for error messages verbatim
   - Evaluate search results by:
     - Recency (prefer last 6-12 months)
     - Source authority (official docs, maintainers)
     - Relevance to current version
   - Look for patterns across multiple sources
   - Check issue trackers & PRs for:
     - Known bugs
     - Breaking changes
     - New features
     - Usage examples
   - Note deprecation notices and API changes

4. Verify features:
   - Test that claimed features exist in source
   - Check method signatures and types
   - Verify CSS properties and selectors
   - Find working examples in tests/examples
   - Document source file locations

5. Implementation:
   - Only use verified features
   - Note source locations in comments
   - Reference test examples
   - Document assumptions
   - Add links to relevant issues/PRs

6. Cross-Validation:
   - Compare source findings with web results
   - Note any discrepancies between docs and source
   - Identify version-specific differences
   - Prefer source code for final decisions
   - Document when web sources helped verify/clarify
   - Create reproducible examples when unsure

## Best Practices

### Source Code First

- ALWAYS start with source code exploration
- Look for concrete implementations, not just interfaces
- Find and read test files for real usage examples
- Document specific file locations and line numbers
- Note any differences between implementation and docs

### Example-Driven Development

- ALWAYS base changes on real examples from source
- Save working examples for future reference
- Note which examples were verified to work
- Document the version where the example was found
- Include links to relevant test files

### Multi-Source Verification

1. Start with source code:

   ```text
   good: find Widget class in source and read implementation
   bad:  assume Widget exists based on docs
   ```

2. Check tests and examples:

   ```text
   good: find test_widget.py showing actual usage
   bad:  copy example from outdated blog post
   ```

3. Validate with web search:

   ```text
   good: "textual v2.1.2 widget implementation example"
   bad:  "how to use textual widget"
   ```

4. Document findings:

   ```text
   good: "Verified in src/textual/widgets.py and March 2025 docs"
   bad:  "Should work based on documentation"
   ```

### Code Changes

- NEVER add features without source verification
- ALWAYS include source references in comments
- Document any workarounds or limitations
- Note which version was tested
- Include relevant issue/PR links

### Error Handling

- Check error cases in source tests
- Document expected error conditions
- Note version-specific error handling
- Test error paths before committing

### Documentation

- Keep source links in comments
- Note verification methods used
- Document any version constraints
- Include links to relevant tests
- Reference related issues/PRs
