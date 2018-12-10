# -*- coding: utf-8 -*-

# Scrapy settings for zhifu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhifu'

SPIDER_MODULES = ['zhifu.spiders']
NEWSPIDER_MODULE = 'zhifu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    ":authority" : 'www.zhihu.com',
    ":method" : 'GET',
    ":path" : '/api/v4/members/liuyu-43-97/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=60&limit=20',
    ":scheme" : 'https',
    "accept" : '*/*',
    # "accept-encoding" : 'gzip, deflate, br',
    "accept-language" : 'zh-CN,zh;q=0.9',
    "cookie" : 'd_c0="AMDmhciC1w2PTraEPDniUU7llNF7MDO3-Gk=|1530580989"; _zap=4d57f55e-f59b-4f47-a54e-4a11dcb81bc9; _xsrf=5D2hr8reJsXtjo68Rg0Vi6V0YT48LeY8; __utmz=51854390.1539756766.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; z_c0="2|1:0|10:1539757464|4:z_c0|92:Mi4xWXNuSERBQUFBQUFBd09hRnlJTFhEU1lBQUFCZ0FsVk5tQ08wWEFDZ2tseEVkanVraVkyNWpkSGpManN6cm5QLTZR|812251d37f4e7c685b777bda8f025482d3e046c473ae78dbc6dc0892c3b239bc"; __utmv=51854390.100--|2=registration_date=20181017=1^3=entry_date=20180703=1; tgw_l7_route=860ecf76daf7b83f5a2f2dc22dccf049; q_c1=4a4da0bbcc084e8b8c3b3bc8f1f61064|1543475400000|1530580989000; __utma=51854390.627634630.1539756766.1539756766.1543475397.2; __utmb=51854390.0.10.1543475397; __utmc=51854390',
    "referer" : 'https://www.zhihu.com/people/liuyu-43-97/followers?page=3',
    "x-ab-param" : 'top_yhgc=0;top_is_gr=0;top_recall=1;top_root_web=0;se_backsearch=0;top_ac_merge=0;top_v_album=1;top_gr_model=0;top_nmt=0;top_rank=1;tp_sft=a;se_qc=0;top_free_content=-1;top_recall_tb=1;top_root=1;top_wonderful=1;se_new_market_search=on;top_rerank_breakin=-1;top_vdio_rew=0;top_dtmt=2;top_feedtopiccard=0;pf_creator_card=0;se_engine=1;tp_ios_topic_write_pin_guide=1;top_billab=0;top_tmt=0;top_tuner_refactor=-1;se_billboard=1;top_tagore=1;top_billread=1;top_newfollowans=0;top_vd_rt_int=0;top_alt=0;top_deep_promo=0;top_vd_gender=0;se_dl=1;top_distinction=0;top_recall_tb_short=61;top_slot_ad_pos=1;tp_discussion_feed_type_android=2;se_sltr=0;top_manual_tag=1;top_billvideo=0;top_retag=0;top_ntr=1;top_video_fix_position=0;top_yc=0;top_retagg=0;se_merger=1;se_ad_index=6;top_billupdate1=3;tp_favsku=b;se_major_onebox=major;top_feedre=1;top_nucc=3;se_consulting_switch=off;top_login_card=1;top_pfq=5;top_gr_auto_model=0;top_nszt=0;top_uit=0;se_ltr=1;top_30=0;top_memberfree=1;se_gemini_service=content;se_minor_onebox=d;se_tf=1;top_new_feed=1;top_f_r_nb=1;top_no_weighing=1;top_nuc=0;top_rerank_isolation=-1;se_rescore=1;top_billboard_count=1;top_raf=y;top_sjre=0;se_majorob_style=0;top_followtop=1;top_hqt=9;tp_discussion_feed_card_type=2;pin_efs=orig;se_ingress=on;top_recommend_topic_card=0;top_roundtable=1;se_product_rank_list=0;top_fqai=2;top_scaled_score=0;top_vd_op=0;top_follow_reason=0;top_billpic=0;top_ebook=0;top_ab_validate=6;top_mt=0;se_websearch=0;top_hweb=0;top_recall_deep_user=1;top_adpar=0;top_tagore_topic=0;top_video_score=1;ls_is_use_zrec=0;pin_ef=orig;top_an=0;se_consulting_price=p;top_new_user_gift=0;top_recall_tb_long=51;top_feedre_cpt=101;top_recall_core_interest=81;top_recall_follow_user=91;top_videos_priority=-1;ls_new_video=1;top_nid=0;top_gr_topic_reweight=0;top_recall_tb_follow=71;top_spec_promo=1;top_test_4_liguangyi=1;top_topic_feedre=21;se_refactored_search_index=0;top_promo=1;top_tag_isolation=0;ls_new_score=1;se_cq=1;top_quality=0;se_auto_syn=0;se_billboardsearch=0;se_time_search=origin;se_wiki_box=1;se_entity=on;top_bill=0;top_mlt_model=0;top_rerank_repos=-1;top_feedre_itemcf=31;top_gif=0;zr_ans_rec=gbrank;top_local=1;top_root_ac=1;se_relevant_query=new;top_feedre_rtt=41;top_fqa=0;top_universalebook=1;top_tffrt=0;top_user_gift=0;tp_write_pin_guide=3;top_newfollow=0;se_cm=1;se_daxuechuisou=new;se_filter=0;top_lowup=1;top_vds_alb_pos=0;top_nad=1;top_root_few_topic=0;top_root_mg=1;se_dt=1;top_tr=0;se_correct_ab=0;se_gi=1;top_cc_at=1;top_sj=2;top_video_rew=0;top_ad_slot=1;top_hca=0;top_multi_model=0;top_rerank_reweight=1;top_card=-1',
    "x-requested-with" : 'fetch',
    "x-udid" : 'AMDmhciC1w2PTraEPDniUU7llNF7MDO3-Gk=',
    "x-zse-83" : '3_1.1',
    "x-zse-84" : 'k_NkRW5lP1rbNorlgg9k0GKlQ9r_KoQljcrwQGtkN58bRc8xyhAl66omOk8b7drl',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhifu.middlewares.ZhifuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'zhifu.middlewares.ZhifuDownloaderMiddleware': 543,
   'zhifu.middlewares.ChangeProxy': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'zhifu.pipelines.ZhifuPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
