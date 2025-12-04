from pybtex.database.input import bibtex

def get_personal_data():
    name = ["Yiran", "Xu"]
    email = "yiranx@umd.edu"
    twitter = "Xu_Arthas"
    github = "twizwei"
    linkedin = "yiran-xu"
    bio_text = f"""
                <p>
                    I'm a research scientist at <a href="https://research.adobe.com/">Adobe Research</a>. 
                    I received my Ph.D. from the <a href="https://umd.edu/">University of Maryland, College Park</a>, 
                    where I was advised by Prof. <a href="https://jbhuang0604.github.io/">Jia-Bin Huang</a>.
                </p>
                <p>
                    My research interests are in computer vision and deep learning, focusing on generative models and their applications, especially in <b>videos</b>.
                </p>
                <p>
                    I've interned at <sup><img src="./assets/img/gdm_logos.svg" width="20"/></sup><a href="https://deepmind.google/">Google DeepMind</a>,
                    <sup><img src="./assets/img/adobe_logo.png" width="15"/></sup><a href="https://research.adobe.com/">Adobe Research</a> 
                    and <sup><img src="./assets/img/snapchat-logo.svg" width="20"/></sup><a href="https://research.snap.com/">Snap Research</a>, 
                    where I had the pleasure of collaborating with many<button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapsecollaborator" aria-expanded="false" aria-controls="collapseExample" style="margin-left: -6px; margin-top: -4px;">talented researchers.</button>
                    <div class="collapse" id="collapsecollaborator">
                        <div class="card card-body">
                                <p>
                                    <sup><img src="./assets/img/gdm_logos.svg" width="35"/></sup> Google DeepMind (2024): 
                                    <a href="https://sites.google.com/view/feng-yang">Feng Yang</a>,
                                    <a href="https://research.google/people/yinxiaoli/?&type=google">Yinxiao Li</a>,
                                    <a href="https://scholar.google.com/citations?user=fKBmhcUAAAAJ&hl=en">Luciano Sbaiz</a>,
                                    <a href="https://scholar.google.com/citations?user=y0sdeykAAAAJ&hl=en">Junjie Ke</a>,
                                    <a href="https://scholar.google.com/citations?user=j99nvycAAAAJ&hl=en">Miaosen Wang</a>,
                                    <a href="https://scholar.google.com/citations?user=72jdrSUAAAAJ&hl=en">Hang Qi</a>,
                                    <a href="https://sites.google.com/view/hanzhang">Han Zhang</a>,
                                    <a href="https://jlezama.github.io/">Jose Lezama</a>,
                                    <a href="https://faculty.ucmerced.edu/mhyang/">Ming-Hsuan Yang</a>,
                                    <a href="https://www.irfanessa.gatech.edu/">Irfan Essa</a>,
                                    <a href="https://scholar.google.com/citations?user=CSHNLDcAAAAJ&hl=en">Jesse Berent</a>.
                                </p>
                                <p>
                                    <sup><img src="./assets/img/adobe_logo.png" width="35"/></sup> Adobe Research (2023): 
                                    <a href="https://difanliu.github.io/">Difan Liu</a>,
                                    <a href="https://taesung.me/">Taesung Park</a>,
                                    <a href="https://richzhang.github.io/">Richard Zhang</a>,
                                    <a href="https://yzhou359.github.io/">Yang Zhou</a>,
                                    <a href="https://research.adobe.com/person/eli-shechtman/">Eli Shechtman</a>,
                                    <a href="https://pages.cs.wisc.edu/~fliu/">Feng Liu</a>.
                                </p>
                                <p>
                                    <sup><img src="./assets/img/adobe_logo.png" width="35"/></sup> Adobe Research (2022): 
                                    <a href="https://sites.google.com/view/seoungwugoh/">Seoung Wug Oh</a>,
                                    <a href="https://zhixinshu.github.io/">Zhixin Shu</a>,
                                    <a href="https://research.adobe.com/person/cameron-smith/">Cameron Smith</a>.
                                </p>
                                <p>
                                    <sup><img src="./assets/img/snapchat-logo.svg" width="35"/></sup> Snap Research (2021): 
                                    <a href="https://alanspike.github.io/">Jian Ren</a>,
                                    <a href="https://zeng.science/">Zeng Huang</a>,
                                    <a href="https://mlchai.com/">Menglei Chai</a>,
                                    <a href="https://kyleolsz.github.io/">Kyle Olszewski</a>,
                                    <a href="http://hsinyinglee.com/">Hsin-Ying Lee</a>,
                                    <a href="http://www.stulyakov.com/">Sergey Tulyakov</a>.
                                </p>
                        </div>
                    </div>
                </p>
                <p>
                    <a href="./assets/other/bio.txt" target="_blank" style="margin-right: 5px"><i class="fa-solid fa-graduation-cap"></i> Bio</a>
                    <a href="./assets/pdf/Yiran_CV.pdf" target="_blank" style="margin-right: 5px"><i class="fa fa-address-card fa-lg"></i> CV</a>
                    <a href="mailto:yiranx@umd.edu" style="margin-right: 5px"><i class="far fa-envelope-open fa-lg"></i> Mail</a>
                    <a href="https://x.com/Xu_Arthas" target="_blank" style="margin-right: 5px"><i class="fa-brands fa-x-twitter"></i>(Twitter)</a>
                    <a href="https://scholar.google.com/citations?user=lyDM3ugAAAAJ&hl=en" target="_blank" style="margin-right: 5px"><i class="fa-solid fa-book"></i> Scholar</a>
                    <a href="http://github.com/twizwei" target="_blank" style="margin-right: 5px"><i class="fab fa-github fa-lg"></i> Github</a>
                    <a href="https://www.linkedin.com/in/yiran-xu-55683816b/" target="_blank" style="margin-right: 5px"><i class="fab fa-linkedin fa-lg"></i> LinkedIn</a>
                </p>
    """
    footer = """
            <div class="col-sm-12" style="">
                <p>
                    The template is from <a href="https://github.com/m-niemeyer/m-niemeyer.github.io" target="_blank">Michael Niemeyer</a>. <br>
                </p>
            </div>
    """
    return name, bio_text, footer

def get_author_dict():
    return {
        'Jia-Bin Huang': 'https://jbhuang0604.github.io/',
        'Taesung Park': 'https://taesung.me/',
        'Richard Zhang': 'https://richzhang.github.io/',
        'Yang Zhou': 'https://yzhou359.github.io/',
        'Eli Shechtman': 'https://research.adobe.com/person/eli-shechtman/',
        'Feng Liu': 'https://pages.cs.wisc.edu/~fliu/',
        'Difan Liu': 'https://difanliu.github.io/',
        'Zhixin Shu': 'https://zhixinshu.github.io/',
        'Cameron Smith': 'https://research.adobe.com/person/cameron-smith/',
        'Seoung Wug Oh': 'https://sites.google.com/view/seoungwugoh/',
        'Yi-Ling Qiao': 'https://ylqiao.net/',
        'Alexander Gao': 'https://www.alexandergao.com/',
        'Yue Feng': 'https://yuefeng21.github.io/',
        'Ming Lin': 'https://www.cs.umd.edu/~lin/',
        'Ting-Hsuan Liao': 'https://tinghliao.github.io/',
        'Songwei Ge': 'https://songweige.github.io/',
        'Yao-Chih Lee': 'https://yaochih.github.io/',
        'Badour AlBahar': 'https://badouralbahar.github.io/',
        'Nuno Vasconcelos': 'http://www.svcl.ucsd.edu/~nuno/',
        'Xiaoyin Yang': 'https://www.linkedin.com/in/xiaoyinyang/',
        'Lihang Gong': 'https://www.linkedin.com/in/lihang-gong/',
        'Hsuan-Chu Lin': 'https://www.linkedin.com/in/hsuan-chu-lin/?locale=en_US',
        'Tz-Ying Wu': 'https://gina9726.github.io/',
        'Yunsheng Li': 'http://www.svcl.ucsd.edu/people/yunsheng/',
        'Yicong Hong': 'https://yiconghong.me/',
        'Yiqun Mei': 'https://yiqunmei.net/',
        'Chongjian Ge': 'https://chongjiange.github.io/',
        'Sai Bi': 'https://sai-bi.github.io/',
        'Yannick Hold-Geoffroy': 'https://yannickhold.com/',
        'Mike Roberts': 'https://mikeroberts3000.github.io/',
        'Matthew Fisher': 'https://techmatt.github.io/',
        'Kalyan Sunkavalli': 'http://www.kalyans.org/',
        'Zhengqi Li': 'https://zhengqili.github.io/',
        'Hao Tan': 'https://www.cs.unc.edu/~airsplay/',
        }

def generate_person_html(persons, connection=", ", make_bold=True, make_bold_name='Yiran Xu', add_links=True):
    links = get_author_dict() if add_links else {}
    s = ""
    for p in persons:
        string_part_i = ""
        for name_part_i in p.get_part('first') + p.get_part('middle') + p.get_part('last'): 
            if string_part_i != "":
                string_part_i += " "
            string_part_i += name_part_i
        # if string_part_i in links.keys():
        #     string_part_i = f'<a href="{links[string_part_i]}" target="_blank">{string_part_i}</a>'
        if make_bold and (string_part_i == make_bold_name or make_bold_name in string_part_i):
            # string_part_i = f'<span style="font-weight: bold";>{make_bold_name}</span>'
            string_part_i = f'<span style="font-weight: bold";>{string_part_i}</span>'
        if p != persons[-1]:
            string_part_i += connection
        s += string_part_i
    return s

def get_paper_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-4">"""
    if 'img' in entry.fields.keys():
        if entry.fields['img'].endswith('.mp4'):
            # autoplay video without controls
            s += f"""<video autoplay loop muted playsinline class="img-fluid img-thumbnail" alt="Project video" style="width: 100%; height: auto;"><source src="{entry.fields['img']}" type="video/mp4"></video>"""
        else:
            s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-8">"""

    if 'award' in entry.fields.keys():
        s += f"""<a href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a> <span style="color: red;">({entry.fields['award']})</span><br>"""
    else:
        s += f"""<a href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a> <br>"""

    s += f"""{generate_person_html(entry.persons['author'])} <br>"""
    if 'Cropper' in entry.fields['title']:
        # Add an additional line to indicate "* means equal contribution"
        s += """<span style="font-style: italic;">*: equal contribution</span> <br>"""
    # Handle both conference papers (booktitle) and journal articles (journal)
    venue = entry.fields.get('journal', entry.fields.get('booktitle', 'Unknown'))
    s += f"""<span style="font-style: italic;">{venue}</span>, {entry.fields['year']} <br>"""
    
    if 'tldr' in entry.fields.keys():
        # make TL;DR bold, and make the text italic
        s += f"""<span style="font-weight: bold;">TL;DR:</span> <span style="font-style: italic;">{entry.fields['tldr']}</span> <br>"""

    artefacts = {'html': 'Project Page', 'pdf': 'Paper', 'supp': 'Supplemental', 'video': 'Video', 'poster': 'Poster', 'code': 'Code', 'media': 'Media Coverage'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')

    # Determine entry type based on available fields
    entry_type = "article" if 'journal' in entry.fields else "inproceedings"
    cite = f"<pre><code>@{entry_type}" + "{" + f"{entry_key}, \n"
    cite += "\tauthor = {" + f"{generate_person_html(entry.persons['author'], make_bold=False, add_links=False, connection=' and ')}" + "}, \n"
    cite += f"\ttitle = " + "{" + f"{entry.fields['title']}" + "}, \n"
    # Add journal or booktitle depending on entry type
    if 'journal' in entry.fields:
        cite += f"\tjournal = " + "{" + f"{entry.fields['journal']}" + "}, \n"
    elif 'booktitle' in entry.fields:
        cite += f"\tbooktitle = " + "{" + f"{entry.fields['booktitle']}" + "}, \n"
    cite += f"\tyear = " + "{" + f"{entry.fields['year']}" + "}, \n"
    cite += """}</pre></code>"""
    s += " /" + f"""<button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse{entry_key}" aria-expanded="false" aria-controls="collapseExample" style="margin-left: -6px; margin-top: -2px;">Expand bibtex</button><div class="collapse" id="collapse{entry_key}"><div class="card card-body">{cite}</div></div>"""
    s += """ </div> </div> </div>"""
    return s

def get_talk_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""
    s += f"""{entry.fields['title']}<br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'slides': 'Slides', 'video': 'Recording'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')
    s += """ </div> </div> </div>"""
    return s

def get_publications_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('publication_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_paper_entry(k, bib_data.entries[k])
    return s

def get_talks_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('talk_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_talk_entry(k, bib_data.entries[k])
    return s

def get_index_html():
    pub = get_publications_html()
    talks = get_talks_html()
    name, bio_text, footer = get_personal_data()
    s = f"""
    <!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />
  <script src="https://kit.fontawesome.com/d0f99e6e70.js" crossorigin="anonymous"></script>
  <title>{name[0] + ' ' + name[1]}</title>
  <link rel="icon" type="image/x-icon" href="assets/favicon.ico">
</head>

<body>
    <!-- Navigation bar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
        <a class="navbar-brand" href="https://twizwei.github.io/"><i class="fas fa-home"></i> {name[0] + ' ' + name[1]}</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <a class="nav-link" href="#bio">Bio</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#publications">Publications</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#service">Service</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#misc">Miscellaneous</a>
            </li>
          </ul>
        </div>
      </nav>
      
    <div class="container" style="margin-top: 80px;">
        <div class="row">
            <div class="col-md-1"></div>
            <div class="col-md-12">
                <div class="row" style="margin-top: 3em;">
                    <div class="col-sm-12" style="margin-bottom: 1em;">
                    <h3 class="display-4" style="text-align: center;"><span style="font-weight: bold;">{name[0]}</span> {name[1]}</h3>
                    </div>
                    <br>
                    <div class="col-md-8 text-justify" style="" id="bio">
                        {bio_text}
                    </div>
                    <div class="col-md-4" style="">
                        <img src="assets/img/profile.JPG" class="img-thumbnail" width="280px" alt="Profile picture">
                    </div>
                </div>
                <div class="row" style="margin-top: 1em;" id="publications">
                    <div class="col-sm-13" style="">
                        <h4>Publications</h4>
                        {pub}
                    </div>
                </div>
                <div class="row" style="margin-top: 1em;" id="service">
                    <div class="col-sm-12" style="">
                        <h4>Service</h4>
                        Reviewer for CVPR'2022-2024, ICCV'2021-2023, ECCV'2022-2024, NeurIPS'2023, ICLR'2024, ICML'2024, WACV'2023-2024, ACCV'2024.
                    </div>
                </div>
                <div class="row" style="margin-top: 3em;" id="misc">
                    <div class="col-sm-12" style="">
                        <h4>Miscellaneous</h4>
                        <p>
                            My Chinese name is 许亦冉. 
                            I was born in <a href="https://en.wikipedia.org/wiki/Hengyang">Hengyang</a>, China, also known as the “Wild Goose City” (雁城). 
                            According to local tales, geese migrating south never go beyond Hengyang because they find the warmest weather here.
                        </p>
                        <p>
                            I have two cats, <a href="./assets/img/bai.jpeg">Bai (白)</a> and <a href="./assets/img/Michelle.jpg">Chelle (锈)</a>.
                            They are important members who keep me company during my PhD journey.
                        </p>
                        <p>
                            I started working on computer vision because I wanted to build a makeup machine for my wife. Well...maybe not that simple.
                        </p>
                        <p>
                            I'm also a newbie in photography. Feel free to check out some of my <a href="./gallery.html">photos</a>!
                        </p>
                    </div>
                </div>
                
                
            </div>
            <div class="col-md-1"></div>
        </div>
    </div>

    

    <footer class="footer bg-dark text-white">
        <div class="container text-center">
            <div class="row" style="margin-top: 1em; margin-bottom: 1em;">
                {footer}
            </div>
            <div class="container text-center mt-1">
                <a href='https://clustrmaps.com/site/1bzwq' title='Visit tracker'>
                    <img src='https://clustrmaps.com/map_v2.png?cl=ffffff&w=a&t=tt&d=yiWnwTDj8JyOXMKUf1le9Gm5fa1aNjrszfMFmu4slDw' alt="Visit tracker"/>
                </a>
            </div>  
        </div>
    </footer>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"></script>
</body>

</html>
    """
    return s


def write_index_html(filename='index.html'):
    s = get_index_html()
    with open(filename, 'w') as f:
        f.write(s)
    print(f'Written index content to {filename}.')

if __name__ == '__main__':
    write_index_html('index.html')