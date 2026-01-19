
import Link from "next/link";

export default function Home() {
  return (
    <div>
      <h1>Neighborhood Library</h1>
      <ul>
        <li><Link href="/books">Books</Link></li>
        <li><Link href="/members">Members</Link></li>
      </ul>
    </div>
  );
}
