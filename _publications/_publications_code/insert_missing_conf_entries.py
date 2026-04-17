from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
PUBLICATIONS_DIR = ROOT / "_publications"

MISSING_ENTRIES = [
    {
        "pub_id": 13,
        "year": 2025,
        "venue": "<em>2025 IEEE International Symposium on Microelectronics and Packaging (ISMP)</em>",
        "title": "Advanced Interconnect Design in 3D-Printed Fan-Out Interposers",
        "authors": "(Haksoon Jung) and Jimin Kwon*",
    },
    {
        "pub_id": 14,
        "year": 2025,
        "venue": "<em>2025 IEEE International Symposium on Microelectronics and Packaging (ISMP)</em>",
        "title": "Reinforcement Learning–Driven Custom Liquid Micro-Channel Design for Direct Liquid Cooling in Advanced Packaging",
        "authors": "Seongju Kim and Jimin Kwon1,2,†",
    },
    {
        "pub_id": 15,
        "year": 2025,
        "venue": "<em>2025 IEEE International Symposium on Microelectronics and Packaging (ISMP)</em>",
        "title": "Continuous-Time Linear Equalization Based on Organic Mixed Ionic–Electronic Conductors",
        "authors": "Yongwoo Lee, Hyeongjun Kim, Yurim Choi, Kyungsun Kim, Haksoon Jung, Sungmin Eum, Seongju Kim, and Jimin Kwon*",
    },
    {
        "pub_id": 16,
        "year": 2025,
        "venue": "<em>2025 IEEE International Symposium on Microelectronics and Packaging (ISMP)</em>",
        "title": "Radio-Frequency Carbon Nanotube Field-Effect Transistors on Glass Substrates",
        "authors": "Sungmin Eum, Yehyun Shin, Seunghun Baek, Yurim Choi, Kyungsun Kim, Haksoon Jung, Yongwoo Lee, and Jimin Kwon",
    },
    {
        "pub_id": 17,
        "year": 2025,
        "venue": "<em>2025 IEEE International Symposium on Microelectronics and Packaging (ISMP)</em>",
        "title": "Development of Silver EHD Jet Printing Design Rules for Reliable RF Component Fabrication",
        "authors": "Hyeongjun Kim, Yongwoo Lee, Seongju Kim, and Jimin Kwon",
    },
    {
        "pub_id": 18,
        "year": 2025,
        "venue": "<em>2025 Korean Institute of Semiconductor and Materials (KISM)</em>",
        "title": "3D-Printed Organic Interposer with Embedded Fan-Out Interconnects Enabled by Additive Manufacturing",
        "authors": "정학순, 권지민",
    },
    {
        "pub_id": 19,
        "year": 2025,
        "venue": "<em>2025 MRS Fall Meeting</em>",
        "title": "Radio-Frequency Signal Transmission in Organic Mixed Ionic-Electronic Conductors",
        "authors": "(Yongwoo Lee), Hyeongjun Kim, Kyungsun Kim, Haksoon Jung, Seongju Kim, Yurim Choi, Sungmin Eum, and Jimin Kwon*",
    },
    {
        "pub_id": 20,
        "year": 2025,
        "venue": "<em>2025 MRS Fall Meeting</em>",
        "title": "Sulfur Vacancy Repair in MoS2 Using Electron-Withdrawing Benzenethiol",
        "authors": "(Haksoon Jung) Mingyu Kim,2 Yongwoo Lee,1 Gi Beom Sim,3 Hyeonho Gu,1 Sumin Hong,4 Sanghyun Lee,1 Jaehyun Lee,5 Donghyeop Lee,5 Taoyu Zou,2 Kibum Kang,5 Chang Woo Myung,3,6 Yong-Young Noh,2 and Jimin Kwon1,4,*",
    },
]

INSERT_COUNT = len(MISSING_ENTRIES)
RENAME_FROM = 13


def update_pub_id_in_file(path: Path, new_pub_id: int):
    text = path.read_text(encoding='utf-8')
    new_text, count = re.subn(r'pub-id:\s*\d+', f'pub-id: {new_pub_id}', text, count=1)
    if count == 0:
        raise ValueError(f"No pub-id found in {path}")
    path.write_text(new_text, encoding='utf-8')


def rename_existing_files():
    files_to_rename = []
    for i in range(RENAME_FROM, RENAME_FROM + INSERT_COUNT + 1):
        old = PUBLICATIONS_DIR / f'conf-{i:03d}.md'
        if old.exists():
            files_to_rename.append(i)

    if not files_to_rename:
        print("No files to rename.")
        return

    for i in sorted(files_to_rename, reverse=True):
        old_path = PUBLICATIONS_DIR / f'conf-{i:03d}.md'
        new_id = i + INSERT_COUNT
        new_path = PUBLICATIONS_DIR / f'conf-{new_id:03d}.md'
        print(f"Renaming {old_path.name} -> {new_path.name}")
        old_path.rename(new_path)
        update_pub_id_in_file(new_path, new_id)


def create_new_files():
    for entry in MISSING_ENTRIES:
        path = PUBLICATIONS_DIR / f'conf-{entry["pub_id"]:03d}.md'
        if path.exists():
            raise FileExistsError(f"Cannot create {path.name} because it already exists")

        content = f"---\npub-id: {entry['pub_id']}\ntype: conference\n    - international-conf\n\nyear: {entry['year']}\n\ntitle: \"{entry['title']}\"\ntitle_url: \"\"\n\nauthors: \"{entry['authors']}\"\n\nstatus: published\nvenue: \"{entry['venue']}\"\n---\n"
        path.write_text(content, encoding='utf-8')
        print(f"Created {path.name}")


def main():
    rename_existing_files()
    create_new_files()
    print("Done.")


if __name__ == '__main__':
    main()
