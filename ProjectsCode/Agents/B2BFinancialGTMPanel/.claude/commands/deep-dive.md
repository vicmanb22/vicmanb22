---
description: Extended consultation with one expert for comprehensive analysis
---

# /deep-dive Command

Get an extended, in-depth consultation with a single expert. This simulates a 1-hour strategy session rather than a quick panel response.

## Process

1. **Get timestamp**: Run `node -e "console.log(new Date().toLocaleString() + ' (Local Time)')"`

2. **Identify the expert**: Match to profiles in CLAUDE.md or experts.json

3. **Gather context**:
   - Check `.claude/contexts/` for relevant saved context
   - Review conversation history for company details
   - Note any gaps in information

4. **Generate deep-dive response** (1500+ words) including:
   - **Situation Assessment**: Detailed analysis of the user's current state
   - **Framework Application**: Full walkthrough of the expert's methodology
   - **Strategic Recommendations**: 5-7 specific, prioritized actions
   - **Implementation Roadmap**: Sequenced steps with dependencies
   - **Success Metrics**: How to measure progress
   - **Risk Factors**: What could go wrong and how to mitigate
   - **Case Study Reference**: Relevant examples from their experience
   - **Follow-up Questions**: 5-10 questions they would ask in a real session

5. **Offer continuation options**:
   - Answer the expert's follow-up questions
   - Get implementation details on specific recommendations
   - Bring in a complementary expert
   - Create an action plan

## Usage

```
/deep-dive April Dunford positioning strategy
```

```
/deep-dive Bo Brustkern private credit portfolio monitoring GTM
```

```
/deep-dive John McMahon enterprise sales process for $100K+ deals
```

## Output Format

```markdown
---

# Deep-Dive Consultation: [Expert Name]
## [Expert Title/Specialty]
**[Timestamp]**

---

## Situation Assessment

[400+ words analyzing the user's current situation, challenges, and opportunities]

---

## Framework Application: [Expert's Framework Name]

[300+ words walking through how their specific methodology applies]

### Step 1: [Framework Step]
[Application to this situation]

### Step 2: [Framework Step]
[Application to this situation]

[Continue for all framework steps]

---

## Strategic Recommendations

### Priority 1: [Recommendation]
**Why**: [Rationale]
**How**: [Specific actions]
**Timeline**: [When to do this]

### Priority 2: [Recommendation]
[Same structure]

[Continue for 5-7 recommendations]

---

## Implementation Roadmap

### Phase 1: [Timeframe] - [Focus]
- [ ] Action 1
- [ ] Action 2
- [ ] Action 3

### Phase 2: [Timeframe] - [Focus]
[Continue]

---

## Success Metrics

| Metric | Current | Target | Timeline |
|--------|---------|--------|----------|
| [Metric 1] | [If known] | [Target] | [When] |
| [Metric 2] | [If known] | [Target] | [When] |

---

## Risk Factors

### Risk 1: [Risk]
**Likelihood**: [High/Medium/Low]
**Impact**: [High/Medium/Low]
**Mitigation**: [How to address]

[Continue for 3-5 risks]

---

## Follow-Up Questions

Before we proceed further, I'd want to understand:

1. [Question about their specific situation]
2. [Question about resources/constraints]
3. [Question about past attempts]
4. [Question about competitive dynamics]
5. [Question about timeline/urgency]

---

## Next Steps

Would you like to:
1. Answer my follow-up questions for more tailored advice
2. Deep-dive on a specific recommendation
3. Bring in [complementary expert] for additional perspective
4. Create a detailed action plan for Priority 1

---
```
