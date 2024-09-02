import Image from "next/image";
import Link from "next/link";

export default function Home() {
  return (
    <main>
      Hello
      <Link href="/dashboard">DashBoard</Link>
    </main>
  );
}
