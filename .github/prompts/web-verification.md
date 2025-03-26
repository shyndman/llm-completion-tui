# Web Search and Verification Guide

You are verifying library features using both source code and web resources.
Follow these practices:

## Search Strategy

1. Version-Specific Searches:

   ```markdown
   GOOD:
   - "textual v2.1.2 feature implementation"
   - "library v2.1.2 changelog"
   - "feature breaking changes v2.1.2"

   BAD:
   - "how to use feature"
   - "library examples"
   - "feature tutorial"
   ```

2. Issue/PR Searches:

   ```markdown
   GOOD:
   - "repo:org/lib feature implementation"
   - "feature in:title is:merged merged:>2024-01-01"
   - "breaking-change label:bug"

   BAD:
   - "feature not working"
   - "help with feature"
   ```

3. Documentation Searches:

   ```markdown
   GOOD:
   - "site:docs.lib.org feature v2.1.2"
   - "feature api reference v2.1.2"
   - "feature migration guide v2.1"

   BAD:
   - "feature docs"
   - "how to implement feature"
   ```

## Multi-Source Verification

1. Priority Order:

   ```markdown
   1. Source code implementation
   2. Test files and examples
   3. Official documentation
   4. Recent PRs and issues
   5. Community discussions
   ```

2. Source Agreement:

   ```markdown
   REQUIRED:
   - Feature exists in source
   - Tests demonstrate usage
   - Docs match implementation
   - No conflicting PRs/issues
   ```

3. Version Alignment:

   ```markdown
   CHECK:
   - Source code version
   - Documentation version
   - Breaking changes
   - Deprecation notices
   ```

## Documentation Process

1. Source Links:

   ```markdown
   INCLUDE:
   - GitHub permalinks to source
   - Test file references
   - PR/Issue links
   - Documentation URLs with versions
   ```

2. Version Info:

   ```markdown
   DOCUMENT:
   - Implementation version
   - Documentation version
   - Breaking changes
   - Compatibility notes
   ```

3. Search Results:

   ```markdown
   RECORD:
   - Search queries used
   - Relevant findings
   - Conflicting information
   - Resolution process
   ```

## Common Verification Paths

1. New Feature:

   ```markdown
   1. Check source implementation
   2. Find test examples
   3. Read official docs
   4. Search recent PRs
   5. Look for known issues
   ```

2. Bug Investigation:

   ```markdown
   1. Search issue tracker
   2. Check breaking changes
   3. Read source tests
   4. Look for workarounds
   5. Check version history
   ```

3. API Changes:

   ```markdown
   1. Compare source versions
   2. Read migration guides
   3. Check deprecation notes
   4. Test in examples
   5. Verify compatibility
   ```

## Required Documentation

All verifications must include:

```python
"""
Multi-source verification:
- Source: [link to source file]
- Tests: [link to test file]
- Docs: [link to versioned docs]
- Issues: [relevant issues/PRs]
- Search: [key search queries]
- Version: [implementation version]
- Status: [current/deprecated/beta]
"""
```

## Search Result Evaluation

1. Recency:

   ```markdown
   PREFER:
   - Last 6 months primary
   - Last 12 months secondary
   - Version-specific content
   - Official releases
   ```

2. Authority:

   ```markdown
   PRIORITY:
   1. Official docs
   2. Core team members
   3. Major contributors
   4. Community examples
   ```

3. Relevance:

   ```markdown
   EVALUATE:
   - Version match
   - Use case similarity
   - Implementation details
   - Error conditions
   ```

## Version Compatibility

1. Check Compatibility:

   ```markdown
   VERIFY:
   - Minimum version
   - Maximum version
   - Breaking changes
   - Required dependencies
   ```

2. Document Support:

   ```markdown
   NOTE:
   - Feature availability
   - Version constraints
   - Known issues
   - Migration needs
   ```
