---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #f5f5f5
color: #333
style: |
  section {
    font-family: 'Helvetica Neue', Arial, 'PingFang TC', 'Microsoft JhengHei', sans-serif;
    padding: 36px 44px;
    font-size: 23px;
    line-height: 1.55;
  }
  ul, ol {
    margin-top: 8px;
    margin-bottom: 8px;
  }
  li {
    margin-bottom: 10px;
    line-height: 1.5;
  }
  li > ul, li > ol {
    margin-top: 5px;
    margin-bottom: 5px;
  }
  li > ul > li, li > ol > li {
    margin-bottom: 5px;
    font-size: 0.92em;
  }
  h1 {
    color: #0b3c5d;
  }
  h2 {
    color: #328cc1;
    margin-top: 0;
    margin-bottom: 12px;
    font-size: 1.5em;
  }
  h3 {
    color: #0b3c5d;
    font-size: 1.1em;
    margin-top: 0;
    margin-bottom: 12px;
  }
  header {
    position: absolute;
    top: 18px;
    right: 44px;
    text-align: right;
    font-size: 0.5em;
    line-height: 1;
    color: #aaa;
    margin: 0;
    padding: 0;
  }
  footer,
  section::after {
    position: absolute;
    bottom: 18px;
    font-size: 0.5em;
    line-height: 1;
    height: auto;
    margin: 0;
    padding: 0;
  }
  footer {
    left: 44px;
    text-align: left;
    color: #777;
  }
  section::after {
    right: 44px;
    text-align: right;
    color: #777;
  }
  blockquote {
    background: transparent;
    border-left: 4px solid #328cc1;
    margin: 1em 0;
    padding: 8px 18px;
    font-style: italic;
    color: inherit;
    opacity: 0.9;
  }
  blockquote::before,
  blockquote::after {
    content: none !important;
  }
  table {
    margin: 10px auto;
    border-collapse: collapse;
    font-size: 15.5px;
    width: 100%;
  }
  th {
    border-bottom: 2px solid #0b3c5d;
    padding: 6px 10px;
    text-align: left;
    background-color: #eaf1f7;
    color: #0b3c5d;
  }
  td {
    padding: 6px 10px;
    border-bottom: 1px solid #dcdcdc;
    vertical-align: top;
  }
  section.lead {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  section.lead h1 {
    margin: 0 0 16px 0;
    font-size: 2.2em;
  }
  section.lead h2 {
    margin: 0 0 16px 0;
  }
  section.lead h3 {
    margin: 0 0 24px 0;
    color: #328cc1;
    font-size: 1.3em;
  }
  section.lead p {
    margin: 0;
    font-size: 0.85em;
    line-height: 1.6;
  }
  section.lead p strong {
    color: #0b3c5d;
  }
  section.lead header,
  section.lead footer,
  section.lead::after {
    display: none !important;
  }
  div.grid-two {
    display: flex;
    gap: 24px;
  }
  div.grid-two > div {
    flex: 1;
  }
header: '軟體工程 (大學部) | 課程綱要 (115-1)'
footer: '薛念林 教授 · 逢甲大學 資訊工程學系'
---

# 軟體工程 (Software Engineering)

### 課程綱要與學習地圖 — 115學年度第一學期 (115-1)

**大學部核心必選修課程**  
授課教師：薛念林 教授 (Prof. Nien-Lin Hsueh)  
逢甲大學 資訊工程學系  
Department of Information Engineering and Computer Science, FCU

---

## 課程全貌與教學理念 (Course Overview & Philosophy)

* **結合理論基礎、現代工具鏈與 AI 典範轉移：**
  * 軟體開發正從傳統手動編寫程式碼，迅速邁向 **AI 輔助與規格驅動工程 (Spec-Driven AI Engineering)**。
  * 本課程兼顧**經典工程嚴謹性**（軟體生命週期、系統架構、品質保證）與**現代工程典範**（生成式 AI 協作、CI/CD 自動化流程管線、實證評測）。
* **課程核心屬性：**
  * **修課對象：** 資訊多元專班。
  * **互動式教學法：** 課堂概念檢驗題 (CCQ) 即時線上作答、架構思辨分析與小組協作研討。

---

## 課程核心學習目標 (CLOs)

* **1. 精通軟體工程核心領域 (Master Core SE Disciplines)：**
  * 深入理解軟體生命週期模型、敏捷與 Scrum、需求規格分析、UML 物件導向塑模與現代架構風格。
* **2. 建立「品質優先」與實證思維 (Quality-First & Empirical Mindset)：**
  * 內化軟體測試方法論（黑箱測試、白箱測試、覆蓋率準則）、自動化持續整合 (CI/CD) 與實證量測。
* **3. 嚴謹且負責任的 AI 協作技能 (Rigorous AI Integration)：**
  * 學會以嚴密規格有效引導 AI 編程代理人 (AI Coding Agents)，驗證生成程式碼，有效防範 AI 幻覺與技術債務。
* **4. 使用者體驗的認識與設計 (User Experience Design)：**
  * 理解以人為本的設計思維與易用性原則 (Usability Heuristics)，掌握操作流程規劃、介面視覺階層與互動原型驗證。

---

## 五大核心課程模組與進度 (Curriculum Roadmap)

* **模組 1：基礎篇 (第 1 週)**
  * 從 1968 年軟體危機到現代軟體工程；從普通程式碼到合格的高品質軟體系統。
* **模組 2：軟體流程與需求工程 (第 2–4 週)**
  * 敏捷開發、Scrum、DevOps、規格驅動 AI 開發流程 (Spec-Driven AI Workflows)。
  * 需求工程（功能性／非功能性規格分析、AI 提示與系統規格書）。
* **模組 3：軟體設計與塑模 (第 5–9 週)**
  * 物件導向設計原則 (SOLID)、設計模式、UML 系統塑模、軟體架構風格。
  * 使用者體驗設計
  * **期中考試 (Midterm Exam)**。
* **模組 4：軟體品質保證與測試 (第 10–13 週)**
  * 測試原理與實務：黑箱測試、白箱測試、覆蓋率準則、單元測試自動化。
  * 軟體專案管理。
* **模組 5：期末專題報告與發表 (第 15–16 週)**
  * 專題成果展示

> ⚠️ **休假提醒：第 3 週 (09/28 教師節補假) 與 第 7 週 (10/26 光復節補假) 為國定假日，停課一次。**

---

## 成績評定標準 (Grading Scheme)

* **20% — 期中考 (Midterm Exam)**
  * 第一階段專業觀念與設計塑模評量
* **20% — 期末考 (Final Exam)**
  * 第二階段品質保證、測試技術與軟工綜合評量
* **20% — 平時課堂互動與問答參與 (In-Class Engagement & QA)**
  * 課堂 CCQ 即時線上作答、同儕論壇提問與實體討論參與度
* **20% — 作業 (Homework)**
* **20% — 期末團隊專題 (Final Capstone Project)**
  * AI 輔助軟體工程實務：完成完整需求分析、架構設計文件與可運行之系統雛形

---

## 期末團隊專題：AI 輔助軟體工程與雛形實作

* **團隊合作形式：** 每組約 **3 位成員**。
* **專案核心目標：**
  * 在 **生成式 AI 的深度輔助下**，完整經歷軟體工程生命週期：需求分析 $\rightarrow$ 系統架構設計 $\rightarrow$ 規格文件產出 $\rightarrow$ 系統雛形 (Working Prototype) 實作。
* **三大核心交付成果 (Project Deliverables)：**
  * **1. 完整需求規格書 (Software Requirements Specification, SRS)：**
    * 包含使用者問題陳述、使用案例 (Use Cases)、功能性與非功能性需求規格。
  * **2. 系統架構與設計書 (Software Design Document, SDD)：**
    * 包含物件導向類別圖、互動循序圖、系統架構分層與介面流程設計。
  * **3. 可運行的軟體雛形系統 (Working Prototype)：**
    * 實現核心業務邏輯的垂直切片 (Thin Vertical Slice) 互動系統。

---

## 專題主題發想指引：領域專業 × AI 賦能 (Domain Expertise + AI)

* **資訊多元專班的獨特優勢：豐富的跨領域與職場經驗 (Domain Knowledge)：**
  * 同學來自不同學術背景與各行各業，深刻了解職場、生活或專業業務中的**真實痛點**。
  * 題目發想請以「**解決真實世界的具體痛點**」為核心，切忌做傳統無感的練習題。
* **善用 AI 槓桿，技術門檻不再是限制（大膽嘗試，不用太客氣！）：**
  * 善用生成式 AI 工具（Claude, Cursor, v0.dev, ChatGPT）快速搭建前端介面與程式邏輯。
  * 重點不在寫出數萬行程式碼，而在於打造能驗證核心價值的**垂直切片雛形 (Working Prototype)**。
* **四大推薦專題方向：**
  * **1. 企業智慧營運與自動化工作流：** 智慧合約審核、採購報價比對、客服與內部知識庫。
  * **2. 智慧健康生活與數位照護：** 慢性病用藥管理、長者遠端照護回報、運動營養個人化引導。
  * **3. 創新商業體驗與顧客互動：** 智慧旅宿行程管家、在地體驗預約平台、會員忠誠互動系統。
  * **4. 日常生活與智慧休閒體驗：** 線上外帶訂餐系統、影城劃位訂票系統、運動場地預約平台。

---

## 專題範例系統 (一)：企業智慧流程 & 數位健康照護

* **範例 A：「企業智慧採購比價與合約審核助手」 (Enterprise AI Workflow)**
  * **業務痛點：** 人工審閱多份廠商報價單與合約耗時費力，容易遺漏異常條款與隱藏成本。
  * **垂直切片流程：** 上傳報價/合約 PDF $\rightarrow$ AI 結構化提取規格與風險 $\rightarrow$ 儀表板並排對比 $\rightarrow$ 一鍵簽核。
  * **UI/UX 亮點：** 清楚直覺的比價矩陣、風險標籤色塊警示、即時流程進度追蹤。
* **範例 B：「高齡長者智慧用藥提醒與照護回報系統」 (Smart Healthcare UX)**
  * **業務痛點：** 慢性病長者多重用藥易混淆或忘記，遠方家屬難以即時確認長輩服藥狀態。
  * **垂直切片流程：** 拍照辨識藥袋建檔 $\rightarrow$ 定時大字體/語音親切提醒 $\rightarrow$ 一鍵確認 $\rightarrow$ LINE 即時回報家屬。
  * **UI/UX 亮點：** 高對比無障礙介面、防呆大按鈕、清晰的確認動畫反饋。

---

## 專題範例系統 (二)：智慧餐飲 & 生活娛樂體驗

* **範例 C：「商圈快點：線上外帶即時訂餐系統」 (Smart Food Ordering & UI/UX)**
  * **業務痛點：** 熱門時段電話點餐常佔線、客製化備註（甜度/冰塊/配料）容易漏單、現場取餐時間不可控。
  * **垂直切片流程：** 瀏覽店家菜單 $\rightarrow$ 彈出式規格客製選擇 $\rightarrow$ AI 推薦升級套餐 $\rightarrow$ 模擬支付 $\rightarrow$ 即時備餐與取餐進度推播。
  * **UI/UX 亮點：** 直覺的分類標籤、一目了然的客製選項防呆、動態訂單進度條（接單 $\rightarrow$ 製作中 $\rightarrow$ 請取餐）。
* **範例 D：「智慧影城線上劃位訂票與餐飲選購系統」 (Everyday Booking & UI/UX)**
  * **業務痛點：** 手機端選位容易誤觸、場次與座位狀態更新不即時、加購餐飲結帳流程繁瑣。
  * **垂直切片流程：** 瀏覽電影與場次 $\rightarrow$ 視覺化互動選位 $\rightarrow$ AI 推薦人氣餐飲加購 $\rightarrow$ 模擬付款 $\rightarrow$ 產出電子票 QR Code。
  * **UI/UX 亮點：** 響應式座位圖防呆縮放、座位暫時鎖定倒數計時、清晰的兩步驟結帳指引。

---

## 期末專題展示與評審重點 (Final Presentation Focus)

* **1. 介面設計與使用者體驗原則 (UI/UX Focus) — 展示核心：**
  * 期末實機展示 (Live Demo) 重點評估：**系統介面的使用是否符合使用者體驗 (UX) 的核心原則**（如操作直覺性、介面一致性、清晰的使用者回饋與防錯機制）。
  * 系統必須提供貼近真實使用者情境、流暢且具說服力的人機互動體驗。
* **2. 需求規格與設計書的完整性與一致性 (Documentation Rigor)：**
  * 報告中**必須充分展示需求規格書與架構設計書的完整性**。
  * 現場 Demo 必須展現雛形系統與設計文件之間的緊密對應（Traceability），證明系統是本於嚴謹規格所建構，而非隨興拼湊。
* **3. 團隊發表與技術答辯：**
  * 清楚說明團隊如何妥善駕馭 AI 工具加速規格產出、降低設計盲點，並展現工程品質。

---

## 學術誠信與生成式 AI 使用規範 (AI Policy)

* **歡迎且鼓勵負責任地運用生成式 AI：**
  * 鼓勵同學在學習與專案中積極運用現代 AI 工具（如 Claude, ChatGPT, GitHub Copilot, Cursor）。
  * **透明公開原則 (Rule of Transparency)：** 凡使用 AI 輔助產生之程式碼、架構設計、測試案例或文稿，皆須在 Commit 訊息或專案附錄中具體記錄使用方式與主要提示詞 (Prompts)。
* **100% 責任承擔原則 (The Accountability Rule)：**
  * **你必須對自己提交的所有程式碼、架構與技術聲明負百分之百的責任**。絕不能將系統當機、資安漏洞或捏造的文獻歸咎於 AI 工具。只要是你提交的，你就必須完全擁有並背書！
* **嚴禁抄襲與剽竊 (Plagiarism)：**
  * 未經正當引用直接抄襲外部開源專案、他人作業或網路文章，一律依校規嚴格處分。

---

## 參考教材與推薦學習資源 (References & Resources)

* **經典核心教材：**
  * Ian Sommerville, *Software Engineering*, 10th Edition, Pearson.（全球經典軟體工程教科書）
  * Robert C. Martin, *Clean Architecture: A Craftsman's Guide to Software Structure and Design*.（整潔架構之道）
  * 精選頂級國際學術會議論文（*ACM/IEEE ICSE, IEEE TSE, ACM TOSEM*）。
* **數位工程工具鏈：**
  * **版本控制與持續整合：** GitHub, GitHub Actions, Docker.
  * **課堂即時互動作答：** NickEduPocket CCQ 雲端互動平台 (`nickedupocket`)。
  * **簡報與講義排版引擎：** Marp Markdown Slide Engine.

---

## 第一週起步指引與行動清單 (Getting Started & Week 1 Action Items)

* **本週立即行動：**
  1. 開始探索感興趣的應用主題，構思如何透過 AI 輔助進行需求分析與系統架構設計。
  2. 開始尋找志同道合的專案夥伴並完成分組（每組約 4 人）。
  3. **國際化多元分組建議：** 鼓勵各組主動邀請班上的外籍生或交換生加入，體驗真實跨國團隊協作。
  4. 每週上課請攜帶筆電或智慧型手機，以利即時參與課堂 CCQ 互動測驗。
* **教師研究室與課後諮詢 (Office Hours)：**
  * **授課教師：** 薛念林 教授 (Prof. Nien-Lin Hsueh)
  * **研究室地點：** 逢甲大學 資訊工程學系系館
  * **聯繫管道：** 歡迎透過課程 LMS 系統或電子郵件預約討論

---

# 提問與交流時間 (Questions & Discussion)

### 歡迎加入軟體工程課程！
### Welcome to Software Engineering!

讓我們在這個學期中，一起打造可靠、優雅且具備長遠影響力的現代軟體系統！
