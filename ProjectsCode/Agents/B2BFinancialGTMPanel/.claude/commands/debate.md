---
description: Request a structured debate between experts with contrasting perspectives
---

# /debate Command

Stage a structured debate between two or more experts who hold contrasting viewpoints on a topic.

## Process

1. **Get timestamp**: Run `node -e "console.log(new Date().toLocaleString() + ' (Local Time)')"`

2. **Identify the debate topic**: Parse the user's request for the core tension or decision

3. **Select debaters** (if not specified by user):
   - Identify 2-3 experts with genuinely different perspectives
   - Choose experts whose frameworks create productive tension
   - Avoid pairing experts who would largely agree

4. **Structure the debate**:
   - **Opening statements** (300 words each): Each expert states their position
   - **Rebuttals** (200 words each): Each expert responds to the others
   - **Synthesis**: Summarize key points of agreement and disagreement
   - **Decision framework**: Help user decide which approach fits their situation

5. **Provide follow-up options**:
   - Deeper consultation with one debater
   - Additional experts to weigh in
   - Action items from the debate

## Usage

```
/debate Sales-led vs. product-led growth for high-ACV financial software
```

```
/debate Enterprise direct sales vs. channel partnerships
```

```
/debate Jason Lemkin vs. Des Traynor on horizontal vs. vertical focus
```

## Common Debate Pairings

| Tension | Expert A | Expert B | Expert C (optional) |
|---------|----------|----------|---------------------|
| Enterprise vs. PLG | John McMahon | Lenny Rachitsky | - |
| Direct vs. Channel | Jill Rowley | Jay McBain | - |
| Vertical vs. Horizontal | Peter Gassner | Des Traynor | - |
| Sales-led vs. Marketing-led | Brent Adamson | Jon Miller | Chris Walker |
| Value pricing vs. Competitive | Madhavan Ramanujam | Patrick Campbell | - |
| Compliance-first vs. Feature-first | Adrienne Fischer | April Dunford | - |

## Output Format

```markdown
---

# Debate: [Topic]
**[Timestamp]**

## The Question
[Frame the core tension in 1-2 sentences]

---

## [Expert A Name] - [Position]

### Opening Statement
[300 words]

### Rebuttal to [Expert B]
[200 words]

---

## [Expert B Name] - [Position]

### Opening Statement
[300 words]

### Rebuttal to [Expert A]
[200 words]

---

## Synthesis

### Points of Agreement
- [Point 1]
- [Point 2]

### Points of Disagreement
- [Point 1]
- [Point 2]

### Decision Framework
When to follow [Expert A]'s approach:
- [Condition 1]
- [Condition 2]

When to follow [Expert B]'s approach:
- [Condition 1]
- [Condition 2]

---
```
