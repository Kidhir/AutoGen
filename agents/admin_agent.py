from agents.report_generator_agent import generate_report

def admin_loop(df, summary, max_attempts=2):
    from agents.critic_agent import review_report

    for attempt in range(max_attempts):
        print(f"\n🔁 Admin Agent: Attempt {attempt + 1}")

        # Step 1: Generate report
        generate_report(summary)
        print("📄 Report regenerated.")

        # Step 2: Critic reviews
        issues = review_report(summary)

        if not issues:
            print("✅ Report passed Critic review!")
            break
        else:
            print("❌ Issues found. Refining report...")
