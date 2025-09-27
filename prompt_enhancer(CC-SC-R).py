import streamlit as st

# Page configuration
st.set_page_config(page_title="Context Engineer", page_icon="📝")
st.title("📝 Context Engineer - CC-SC-R Framework")
st.caption("Demo Mode - Learn how to structure better prompts using Context, Constraint, Structure, Checkpoint & Review!")

# Sidebar with framework explanation
with st.sidebar:
    st.header("CC-SC-R Framework")
    st.markdown("""
    **Context**: Background & situation
    p
    **Constraint**: Limitations & requirements
    
    **Structure**: Output format & organization
    
    **Checkpoint**: Validation & progress points
    
    **Review**: Final evaluation & approval
    """)

st.subheader("🔧 Define Your CC-SC-R Components")

# CC-SC-R Input Fields
context = st.text_area(
    "📍 Context", 
    value="I am researching market trends for a new product launch...",
    help="Provide background information and situational context"
)

constraint = st.text_area(
    "🚧 Constraints", 
    value="Must comply with industry regulations, budget under $50K...",
    help="Define limitations, policies, compliance requirements"
)

structure = st.text_area(
    "🏗️ Structure", 
    value="Provide response in 5 bullet points with supporting data...",
    help="Specify the exact format and organization of the output"
)

checkpoint = st.text_area(
    "✅ Checkpoint", 
    value="Confirm target audience assumptions before proceeding...",
    help="Define validation points and clarifications needed"
)

review = st.text_area(
    "📋 Review Protocols", 
    value="Require approval from marketing team before implementation...",
    help="Define human approval points and quality gates"
)

st.subheader("✍️ Your Draft Prompt")
draft = st.text_area(
    "Enter your rough prompt:", 
    height=140,
    placeholder="Type your initial prompt idea here..."
)

# Enhanced prompt generation
if st.button("🚀 Enhance Prompt with CC-SC-R", type="primary"):
    if not draft.strip():
        st.warning("⚠️ Please enter a draft prompt to enhance it.")
    else:
        # Generate structured output using CC-SC-R framework
        st.success("✨ Enhanced Prompt Generated!")
        
        # Display the enhanced prompt structure
        enhanced_prompt = f"""
**ENHANCED PROMPT USING CC-SC-R FRAMEWORK**

---

**CONTEXT:**
{context}

**CONSTRAINTS:**
{constraint}

**ORIGINAL PROMPT:**
{draft}

**STRUCTURED OUTPUT REQUIREMENTS:**
{structure}

**CHECKPOINT VALIDATIONS:**
{checkpoint}

**REVIEW PROTOCOLS:**
{review}

---

**FINAL STRUCTURED PROMPT:**

Given the context: {context.split('.')[0]}...

With these constraints: {constraint.split('.')[0]}...

Please {draft.lower()}

**Output Format:** {structure.split('.')[0]}...

**Before proceeding, please confirm:** {checkpoint.split('.')[0]}...

**Review Requirements:** {review.split('.')[0]}...
"""
        
        st.code(enhanced_prompt, language="markdown")
        
        # Show comparison
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📝 Original Prompt")
            st.info(draft)
        
        with col2:
            st.subheader("⚡ CC-SC-R Benefits")
            st.success("""
            ✅ Clear context established
            ✅ Constraints defined
            ✅ Output structure specified
            ✅ Validation points added
            ✅ Review process outlined
            """)
        
        # Additional insights
        st.subheader("🎯 Prompt Quality Insights")
        
        insights_col1, insights_col2, insights_col3 = st.columns(3)
        
        with insights_col1:
            st.metric("Context Clarity", "High", "📈")
            
        with insights_col2:
            st.metric("Structure Score", "Complete", "✅")
            
        with insights_col3:
            st.metric("Review Gates", "Defined", "🔒")

# Footer information
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
💡 <strong>Demo Mode:</strong> This shows how CC-SC-R framework structures your prompts for better results.<br>
In production mode, this would integrate with AI APIs for dynamic enhancement.
</div>
""", unsafe_allow_html=True)