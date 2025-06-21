def review_report(summary, comments_file="outputs/critic_review.md"):
    issues = []

    # Basic rule-based checks for report quality
    if summary.isnull().values.any():
        issues.append("❗ The summary contains missing values.")
    if summary.shape[0] < 3:
        issues.append("⚠️ Not enough statistical insights.")

    # Write review comments
    with open(comments_file, "w") as f:
        f.write("# Critic Agent Review\n\n")
        if not issues:
            f.write("✅ The report looks good! No major issues found.\n")
        else:
            f.write("The report has the following issues:\n")
            for issue in issues:
                f.write(f"- {issue}\n")

    return issues
