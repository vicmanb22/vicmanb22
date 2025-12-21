---
description: Consult a specific expert from the panel
---

# /expert Command

Get a focused response from a specific expert on the panel.

## Process

1. **Get timestamp**: Run `node -e "console.log(new Date().toLocaleString() + ' (Local Time)')"`

2. **Identify the expert**: Match the requested name to the expert profiles in CLAUDE.md or experts.json

3. **Generate extended response**: The expert provides 800+ words (longer than panel responses) including:
   - Timestamp
   - Deep analysis of the situation
   - Full application of their framework
   - Specific, actionable recommendations
   - Relevant case studies or examples
   - Detailed next steps
   - Questions they would ask in a real consultation

4. **Offer follow-up options**:
   - Ask the same expert a follow-up question
   - Get a contrarian view from another expert
   - Request the full panel weigh in

## Usage

```
/expert Jason Lemkin How do I get from $500K to $2M ARR?
```

```
/expert April Dunford Help me position against Chronograph
```

```
/expert Bo Brustkern What covenant monitoring features matter most to private credit funds?
```

## Available Experts

Reference CLAUDE.md for full list. Key experts by category:

**GTM Strategy**: Jason Lemkin, Peter Gassner, Jill Rowley, Mark Organ
**Enterprise Sales**: John McMahon, Brent Adamson, Janice Mars
**Positioning**: April Dunford, Des Traynor, Bob Moesta
**Financial Services**: Ron Shevlin, Mary Wisniewski, Jim Marous
**VC/Investor**: Samir Kaji, Elizabeth Yin, David Teten
**Private Credit**: Bo Brustkern, Peter Renton
**Accounting**: Allan Koltin, Michael Cohn, Jim Boomer
**Pricing**: Madhavan Ramanujam, Kyle Poyar, Patrick Campbell
**Growth**: Casey Winters, Andrew Chen, Lenny Rachitsky

## If Expert Not Found

If the requested expert name doesn't match:
1. Suggest the closest matching expert(s)
2. List experts in the relevant category
3. Offer to proceed with the suggested expert
