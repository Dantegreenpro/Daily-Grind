import sqlite3
from pathlib import Path
from datetime import date, datetime
import argparse
import sys

DB = Path("expenses.db")

def get_conn():
    conn = sqlite3.connect(DB)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS expense(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dt TEXT NOT NULL,              -- ISO date YYYY-MM-DD
            amount REAL NOT NULL CHECK(amount >= 0),
            category TEXT NOT NULL,
            note TEXT
        )
    """)
    return conn

def parse_date(s: str) -> str:
    """Return ISO date (YYYY-MM-DD). Accepts '', 'YYYY-MM-DD', or 'MM/DD/YYYY'."""
    if not s:
        return date.today().isoformat()
    for fmt in ("%Y-%m-%d", "%m/%d/%Y"):
        try:
            return datetime.strptime(s, fmt).date().isoformat()
        except ValueError:
            pass
    sys.exit("❌ Invalid date. Use YYYY-MM-DD or MM/DD/YYYY.")

def cmd_add(args):
    dt = parse_date(args.date or "")
    try:
        amount = float(args.amount)
    except ValueError:
        sys.exit("❌ Amount must be a number.")
    if amount < 0:
        sys.exit("❌ Amount must be ≥ 0.")

    with get_conn() as conn:
        conn.execute(
            "INSERT INTO expense (dt, amount, category, note) VALUES (?, ?, ?, ?)",
            (dt, amount, args.category.strip(), (args.note or "").strip() or None)
        )
    print(f"✓ Added: {dt} ${amount:.2f} [{args.category}] {args.note or ''}".strip())

def cmd_list(args):
    q = "SELECT id, dt, amount, category, COALESCE(note,'') FROM expense"
    params = []
    filters = []

    if args.month:
        # month as YYYY-MM
        try:
            y, m = args.month.split("-")
            datetime(int(y), int(m), 1)  # validate
        except Exception:
            sys.exit("❌ Month must be YYYY-MM (e.g., 2025-09).")
        filters.append("substr(dt,1,7) = ?")
        params.append(args.month)

    if args.category:
        filters.append("LOWER(category) = LOWER(?)")
        params.append(args.category)

    if filters:
        q += " WHERE " + " AND ".join(filters)
    q += " ORDER BY dt DESC, id DESC"

    with get_conn() as conn:
        rows = conn.execute(q, params).fetchall()

    if not rows:
        print("No expenses found.")
        return

    total = 0.0
    print(f"{'ID':>4}  {'Date':<10}  {'Amount':>8}  {'Category':<12}  Note")
    print("-"*60)
    for _id, dt, amt, cat, note in rows:
        total += amt
        print(f"{_id:>4}  {dt:<10}  ${amt:>7.2f}  {cat:<12}  {note}")
    print("-"*60)
    print(f"Total: ${total:.2f}")

def cmd_report(args):
    # Report totals per category for a month
    if not args.month:
        sys.exit("❌ Please provide --month YYYY-MM for report.")
    try:
        y, m = args.month.split("-")
        datetime(int(y), int(m), 1)
    except Exception:
        sys.exit("❌ Month must be YYYY-MM (e.g., 2025-09).")

    with get_conn() as conn:
        rows = conn.execute(
            """
            SELECT category, SUM(amount) AS total
            FROM expense
            WHERE substr(dt,1,7) = ?
            GROUP BY category
            ORDER BY total DESC
            """,
            (args.month,)
        ).fetchall()

    if not rows:
        print("No data for that month.")
        return

    month_total = sum(t for _, t in rows)
    print(f"Report for {args.month}")
    print("-"*36)
    for cat, total in rows:
        pct = (total / month_total) * 100 if month_total else 0
        print(f"{cat:<12}  ${total:>8.2f}  ({pct:>5.1f}%)")
    print("-"*36)
    print(f"Monthly total: ${month_total:.2f}")

def cmd_delete(args):
    with get_conn() as conn:
        cur = conn.execute("DELETE FROM expense WHERE id = ?", (args.id,))
        if cur.rowcount == 0:
            print("⚠️  No such ID.")
        else:
            print(f"🗑  Deleted expense #{args.id}.")

def build_parser():
    p = argparse.ArgumentParser(description="Expense Tracker (SQLite)")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add", help="Add a new expense")
    a.add_argument("amount", help="Amount in dollars, e.g. 12.50")
    a.add_argument("category", help="Category, e.g. food, gas, rent")
    a.add_argument("-n", "--note", help="Optional note")
    a.add_argument("-d", "--date", help="Date (YYYY-MM-DD or MM/DD/YYYY); default today")
    a.set_defaults(func=cmd_add)

    l = sub.add_parser("list", help="List expenses")
    l.add_argument("-m", "--month", help="Filter by month YYYY-MM")
    l.add_argument("-c", "--category", help="Filter by category")
    l.set_defaults(func=cmd_list)

    r = sub.add_parser("report", help="Monthly totals per category")
    r.add_argument("-m", "--month", required=True, help="Month YYYY-MM")
    r.set_defaults(func=cmd_report)

    d = sub.add_parser("delete", help="Delete by ID")
    d.add_argument("id", type=int, help="Expense ID from the list view")
    d.set_defaults(func=cmd_delete)

    return p

if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
